# Longest Strictly Increasing or Strictly Decreasing Subarray
# Difficulty: Easy
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

# Iterate through the array, keeping track of the current lengths of strictly increasing and strictly decreasing subarrays.
# Update the overall maximum length at each step. Reset a counter when its trend breaks.

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        max_overall_length = 1
        current_increasing_length = 1
        current_decreasing_length = 1

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                current_increasing_length += 1
                current_decreasing_length = 1  # Decreasing trend broken
            elif nums[i] < nums[i-1]:
                current_decreasing_length += 1
                current_increasing_length = 1  # Increasing trend broken
            else:  # nums[i] == nums[i-1]
                current_increasing_length = 1  # Both trends broken
                current_decreasing_length = 1

            max_overall_length = max(max_overall_length, current_increasing_length, current_decreasing_length)

        return max_overall_length