# Climbing Stairs II
# Difficulty: Medium
# https://leetcode.com/problems/climbing-stairs-ii/

# Dynamic programming approach. dp[i] represents the minimum cost to reach step i.
# To compute dp[i], consider jumps from i-1, i-2, and i-3, adding the step's cost and jump distance squared.
# The costs array is 1-indexed for steps, so costs[k] refers to input_costs[k-1].

class Solution:
    def climbingStairsII(self, n: int, costs: list[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            current_step_cost = costs[i-1] # costs array