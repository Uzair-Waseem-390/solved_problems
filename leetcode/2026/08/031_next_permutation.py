# Next Permutation
# Difficulty: Medium
# https://leetcode.com/problems/next-permutation/

# Find the largest index i such that nums[i] < nums[i + 1]. If no such index exists, reverse the entire array.
# Otherwise, find the largest index j such that nums[j] > nums[i], swap nums[i] and nums[j], then reverse the subarray nums[i + 1:].
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)

        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1