# Minimum Cost to Acquire Required Items
# Difficulty: Medium
# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total_cost = 0

        # Determine the number of items that contribute to both requirements
        # These are the items that satisfy min(need1, need2) units of both types
        common_requirements_count = min(need1, need2)

        # Calculate the most efficient way to acquire one unit of both type 1 and type 2:
        # Either buy one item of type 3 (costBoth)
        # Or buy one item of type 1 and one item of type 2 (cost1 + cost2)