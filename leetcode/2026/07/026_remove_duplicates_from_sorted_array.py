# Remove Duplicates from Sorted Array
# Difficulty: Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# The array is sorted, so duplicates are adjacent. A two-pointer approach is suitable: one to read elements and another to write unique elements in-place.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        unique_elements_count = 1

        for current_element_index in range(1, len(nums)):
            if nums[current_element_index] != nums[unique_elements_count - 1]:
                nums[unique_elements_count] = nums[current_element_index]
                unique_elements_count += 1
        
        return unique_elements_count