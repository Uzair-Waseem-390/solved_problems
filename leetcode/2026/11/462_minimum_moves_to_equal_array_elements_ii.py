# Minimum Moves to Equal Array Elements II
# Difficulty: Medium
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

# The problem asks to minimize the sum of absolute differences from a target value. This is a classic property where the optimal target value is the median of the array elements.
# The strategy is to sort the array, find the median element, and then calculate the total moves by summing the absolute differences from this median.
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        total_moves = 0
        for num in nums:
            total_moves += abs(num - median)
        return total_moves