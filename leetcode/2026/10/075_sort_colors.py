# Sort Colors
# Difficulty: Medium
# https://leetcode.com/problems/sort-colors/

# Use the Dutch National Flag algorithm with three pointers (low, mid, high)
# to sort 0s, 1s, and 2s in a single pass in-place.
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        low = 0
        mid = 0
        high = n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else: # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1