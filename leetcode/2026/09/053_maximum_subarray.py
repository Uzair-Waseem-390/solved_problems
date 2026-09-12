# Maximum Subarray
# Difficulty: Medium
# https://leetcode.com/problems/maximum-subarray/

# Kadane's algorithm provides an O(n) dynamic programming solution by tracking the maximum sum ending at the current position.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_max_sum = nums[0]
        global_max_sum = nums[0]

        for i in range(1, len(nums)):
            current_max_sum = max(nums[i], current_max_sum + nums[i])
            global_max_sum = max(global_max_sum, current_max_sum)

        return global_max_sum