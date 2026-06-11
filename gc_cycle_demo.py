"""
gc_cycle_demo.py
~~~~~~~~~~~~~~~~
Demonstrates how circular references keep objects "alive" (refcount > 0)
even after every user-accessible name is deleted, and how the cyclic
garbage collector is the only thing that can reclaim them.
"""

import gc
import sys
import ctypes  # lets us peek at an object even after 'del'


# ──────────────────────────────────────────────
# 0.  Helpers
# ──────────────────────────────────────────────
DIVIDER  = "─" * 60
SECTION  = lambda title: print(f"\n{'═'*60}\n  {title}\n{'═'*60}")


def refcount(obj):
    """Return the true reference count minus the 1 added by getrefcount()."""
    return sys.getrefcount(obj) - 1          # -1 for the temp arg inside getrefcount


# ──────────────────────────────────────────────
# 1.  The Node class — simple, but has __del__
#     so we can SEE exactly when Python destroys it
# ──────────────────────────────────────────────
class Node:
    def __init__(self, name: str):
        self.name = name
        self.link = None

    def __repr__(self):
        linked_to = self.link.name if self.link else "None"
        return f"Node(name={self.name!r}, link→{linked_to})"

    def __del__(self):
        # This fires when CPython's reference count actually hits 0
        print(f"    💀  __del__ called  →  Node '{self.name}' is truly destroyed")


# ──────────────────────────────────────────────
# 2.  Create nodes and form a cycle
# ──────────────────────────────────────────────
SECTION("STEP 1 — Create nodes and wire the cycle")

gc.disable()          # turn off automatic GC so nothing is collected behind our back

A = Node("A")
B = Node("B")

print(f"  Created : {A}")
print(f"  Created : {B}")
print(f"\n  Ref-count of A before cycle : {refcount(A)}")
print(f"  Ref-count of B before cycle : {refcount(B)}")

A.link = B            # A  ──►  B
B.link = A            # B  ──►  A   ← closes the cycle

print(f"\n  After A.link = B  and  B.link = A  (cycle formed):")
print(f"  {A}")
print(f"  {B}")


# ──────────────────────────────────────────────
# 3.  Inspect reference counts BEFORE deletion
# ──────────────────────────────────────────────
SECTION("STEP 2 — Inspect reference counts (before del)")

# Each node is referenced by:
#   • the local variable (A or B)          → 1
#   • the other node's .link attribute     → 1
# Total real refs = 2 for each

print(f"  sys.getrefcount(A) raw value : {sys.getrefcount(A)}")
print(f"  Adjusted ref-count of A      : {refcount(A)}  "
      f"  (1 local var  +  1 from B.link)")
print()
print(f"  sys.getrefcount(B) raw value : {sys.getrefcount(B)}")
print(f"  Adjusted ref-count of B      : {refcount(B)}  "
      f"  (1 local var  +  1 from A.link)")


# ──────────────────────────────────────────────
# 4.  Save the raw memory addresses before we delete
# ──────────────────────────────────────────────
id_A = id(A)
id_B = id(B)

print(f"\n  Memory address of A : 0x{id_A:016x}")
print(f"  Memory address of B : 0x{id_B:016x}")


# ──────────────────────────────────────────────
# 5.  Delete the only user-accessible names
# ──────────────────────────────────────────────
SECTION("STEP 3 — del A  and  del B  (the names, NOT the objects)")

print("  (Watch for 💀 — if __del__ fires here the objects were destroyed now)")
print()
del A
del B
print()
print("  Both names deleted. No 💀 appeared — objects are still alive!")
print("  The cycle keeps each node's refcount at 1, preventing destruction.")


# ──────────────────────────────────────────────
# 6.  Prove the objects still exist in memory
# ──────────────────────────────────────────────
SECTION("STEP 4 — Investigate: objects still exist in memory")

# gc.get_objects() returns every object tracked by the cyclic GC
tracked = gc.get_objects()

ghost_A = next((o for o in tracked if isinstance(o, Node) and o.name == "A"), None)
ghost_B = next((o for o in tracked if isinstance(o, Node) and o.name == "B"), None)

if ghost_A and ghost_B:
    print("  ✅  Found both nodes inside gc.get_objects():")
    print(f"      {ghost_A}   id=0x{id(ghost_A):016x}  (matches saved id_A: {id(ghost_A)==id_A})")
    print(f"      {ghost_B}   id=0x{id(ghost_B):016x}  (matches saved id_B: {id(ghost_B)==id_B})")
    print()
    print(f"  Ref-count of ghost_A via ctypes : "
          f"{ctypes.c_long.from_address(id_A).value}")
    print(f"  Ref-count of ghost_B via ctypes : "
          f"{ctypes.c_long.from_address(id_B).value}")
    print()
    print("  Both counts are ≥ 1 — the cycle keeps them pinned.")
    print("  Normal reference-counting CANNOT free them.")
else:
    print("  ⚠  Could not locate nodes (GC may have already collected them).")

# Release our gc investigation references so they don't skew the collect
del ghost_A, ghost_B, tracked


# ──────────────────────────────────────────────
# 7.  Force the cyclic GC to collect
# ──────────────────────────────────────────────
SECTION("STEP 5 — Force gc.collect() to break the cycle")

print("  Calling gc.collect() …")
print()
collected = gc.collect()
print()
print(DIVIDER)
print(f"  ♻️   gc.collect() reclaimed {collected} unreachable object(s).")
print(DIVIDER)


# ──────────────────────────────────────────────
# 8.  Confirm they are gone
# ──────────────────────────────────────────────
SECTION("STEP 6 — Confirm the objects are gone")

tracked_after = gc.get_objects()
still_alive   = [o for o in tracked_after if isinstance(o, Node)]

if still_alive:
    print(f"  ⚠  {len(still_alive)} Node(s) still tracked — unexpected!")
else:
    print("  ✅  No Node objects remain in gc.get_objects().")
    print("  Both nodes have been fully destroyed by the garbage collector.")


# ──────────────────────────────────────────────
# 9.  Summary
# ──────────────────────────────────────────────
SECTION("SUMMARY")
print("""
  ┌─────────────────────────────────────────────────────┐
  │  Phase                │  What happened               │
  ├─────────────────────────────────────────────────────┤
  │  After A.link=B, B.link=A │  refcount(A)==2, refcount(B)==2  │
  │  After del A, del B       │  refcount drops to 1 each        │
  │                           │  (only the cycle holds them)     │
  │  Objects "dead"?          │  Yes — unreachable from code     │
  │  Refcount == 0?           │  NO — cycle keeps it at 1        │
  │  __del__ fired?           │  Not until gc.collect()          │
  │  gc.collect() result      │  Freed both + the cycle itself   │
  └─────────────────────────────────────────────────────┘

  Key lesson: CPython's reference counting alone CANNOT free
  objects involved in a reference cycle.  The supplementary
  cyclic garbage collector (gc module) is required.
""")

gc.enable()   # restore default behaviour
