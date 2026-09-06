# Jump Game II
# Difficulty: Medium
# https://leetcode.com/problems/jump-game-ii/

# This problem can be solved using a greedy approach. We track the farthest point reachable with the current number of jumps
# and the absolute farthest point reachable by considering all possible jumps from the current segment.
# When we reach the boundary of the current jump's reach, we increment the jump count and update our reach boundary.
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jumps_count = 0
        current_reach_boundary = 0
        max_reach_possible = 0

        for i in range(n - 1):
            max_reach_possible = max(max_reach