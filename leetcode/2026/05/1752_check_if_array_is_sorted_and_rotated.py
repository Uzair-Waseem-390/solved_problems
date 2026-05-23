# Check if Array Is Sorted and Rotated
# Difficulty: Easy
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

# The array can be sorted and rotated if there is at most one "break" point (where nums[i] > nums[i+1]),
# and if there is one break, the last element must be less than or equal to the first element to complete the rotation.

class Solution:
    def check(self, nums: list[int]) -> bool:
        disorder_count = 0
        n = len(nums)

        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                disorder_count += 1
        
        if disorder_count == 0:
            return True
        elif disorder_count == 1:
            return nums[n-1] <= nums[0]
        else:
            return False