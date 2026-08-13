# Remove Element
# Difficulty: Easy
# https://leetcode.com/problems/remove-element/

# two-pointer approach: one pointer iterates through the array, the other places non-`val` elements at the beginning
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k