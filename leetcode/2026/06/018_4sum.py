# 4Sum
# Difficulty: Medium
# https://leetcode.com/problems/4sum/

# Sort the array first to efficiently handle duplicates and use the two-pointer approach.
# Iterate with two outer loops, then use two pointers for the remaining pair, similar to 3Sum.
# Crucially, skip duplicate elements at each level to ensure unique quadruplets.

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        quadruplets = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Optimization: If the smallest possible sum with nums[i] is already greater than target, break