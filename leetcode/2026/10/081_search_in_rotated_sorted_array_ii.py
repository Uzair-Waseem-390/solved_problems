# Search in Rotated Sorted Array II
# Difficulty: Medium
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# Binary search with a special case for duplicates to handle scenarios where nums[low], nums[mid], and nums[high] are all equal.
# This duplicate handling might degrade worst-case performance to O(N) but maintains O(logN) on average.
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return True

            # Handle the case where nums[low], nums[mid], and nums[high] are identical.
            # We cannot determine which half is