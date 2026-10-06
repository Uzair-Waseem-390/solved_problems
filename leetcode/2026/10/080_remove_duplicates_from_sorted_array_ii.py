# Remove Duplicates from Sorted Array II
# Difficulty: Medium
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# Two-pointer approach: one pointer (`write_index`) tracks the position for the next valid element, ensuring no more than two occurrences, while the other (`read_index`) iterates through the array.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        write_index = 2

        for read_index in range(2, len(nums)):
            if nums[read_index] != nums[write_index - 2]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index