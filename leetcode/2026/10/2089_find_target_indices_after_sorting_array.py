# Find Target Indices After Sorting Array
# Difficulty: Easy
# https://leetcode.com/problems/find-target-indices-after-sorting-array/

# First sort the array, then iterate through the sorted array to find all indices that match the target value.
# Collect these indices in a list and return it.

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        target_indices = []
        for index in range(len(nums)):
            if nums[index] == target:
                target_indices.append(index)
        return target_indices