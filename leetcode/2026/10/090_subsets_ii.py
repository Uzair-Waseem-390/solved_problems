# Subsets II
# Difficulty: Medium
# https://leetcode.com/problems/subsets-ii/

# Backtracking approach. Sort the input array first to group duplicates.
# Use a `start_index` to manage the recursive calls and ensure elements are considered in order.
# Skip duplicate elements at the current level of recursion to avoid duplicate subsets.

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        all_subsets = []
        current_subset = []
        nums.sort()

        def backtrack(start_index):
            all_subsets.append(list(current_subset))

            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                
                current_subset.append(nums[i])
                backtrack(i + 1)
                current_subset.pop()

        backtrack(0)
        return all_subsets