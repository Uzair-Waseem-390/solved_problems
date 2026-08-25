# Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# This problem requires two modified binary searches: one to find the first occurrence of the target, and another to find the last occurrence.
# A helper function can abstract this logic, using a flag to determine whether to search for the leftmost or rightmost boundary.

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_extreme_index(nums_array: list[int], target_val: int, find_left: bool) -> int:
            extreme_index = -1
            low = 0
            high = len(nums_array) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if nums_array[mid] == target_val:
                    extreme_index = mid
                    if find_left:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums_array[mid] < target_val:
                    low = mid + 1
                else:  # nums_array[mid] > target_val
                    high = mid - 1
            return extreme_index

        first_position = find_extreme_index(nums, target, True)
        if first_position == -1:
            return [-1, -1]
        
        last_position = find_extreme_index(nums, target, False)
        
        return [first_position, last_position]