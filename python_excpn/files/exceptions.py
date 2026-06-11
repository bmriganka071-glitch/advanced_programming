"""
Custom exceptions for the user onboarding validation module.

Hierarchy:
  InvalidEmailError  → ValueError   (bad input value, checked-style)
  UnderageError      → RuntimeError (policy violation, unchecked-style)
"""


class InvalidEmailError(ValueError):
    """
    Raised when a supplied e-mail address is null/empty or fails
    the RFC-5321-inspired regex check.

    Inherits from ValueError because the caller supplied a value that
    is syntactically or structurally wrong — analogous to Java's
    checked IOException hierarchy.
    """

    def __init__(self, email: str, reason: str) -> None:
        self.email = email
        self.reason = reason
        super().__init__(
            f"Invalid email address {email!r}: {reason}"
        )


class UnderageError(RuntimeError):
    """
    Raised when an applicant is below the minimum registration age.

    Inherits from RuntimeError because it represents a *policy*
    violation that the caller should not routinely try to catch and
    recover from — analogous to Java's unchecked RuntimeException
    hierarchy.
    """

    MINIMUM_AGE: int = 18

    def __init__(self, age: int) -> None:
        self.age = age
        super().__init__(
            f"Applicant is {age} year(s) old, but must be at least "
            f"{self.MINIMUM_AGE} to register."
        )
