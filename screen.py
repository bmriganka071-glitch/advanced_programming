from typing import List, Dict, Set
from collections import defaultdict
from functools import reduce

# Total screen time per user
def total_time_per_user(logs: List[Dict]) -> Dict[str, float]:

    user_time = defaultdict(float)

    def reducer(acc, log):
        acc[log["user"]] += log["duration"]
        return acc

    return reduce(reducer, logs, user_time)


# Top K most active users
def most_active_users(logs: List[Dict], k: int) -> List[str]:

    user_time = total_time_per_user(logs)

    sorted_users = sorted(
        user_time.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [user for user, _ in sorted_users[:k]]


# All unique actions
def unique_actions(logs: List[Dict]) -> Set[str]:

    return {log["action"] for log in logs}


# Example usage
logs = [
    {"user": "101", "action": "YouTube", "duration": 1.5},
    {"user": "102", "action": "Instagram", "duration": 2.0},
    {"user": "101", "action": "WhatsApp", "duration": 0.5},
    {"user": "103", "action": "YouTube", "duration": 3.0},
    {"user": "102", "action": "Chrome", "duration": 1.2},
]

print("Total time per user:", total_time_per_user(logs))
print("Top 2 active users:", most_active_users(logs, 2))
print("Unique actions:", unique_actions(logs))


# Compute total time : O(n)        # n = number of logs 
#Time complexity for sorting u users: O(u log u)
# time complexity for selcting k users : O(k)
# Final complexity :O(n + u log u)
# Worst case (Every log is different):O(nlogn)

# Space complexity for u users : O(u)
# Unique actions set : O(a)
# Final space complexity : O(u + a)
# Worst case complexity : O(u)
