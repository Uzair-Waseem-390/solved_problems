# Subsets
# Difficulty: Medium
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # Recursive backtracking approach explores all possibilities by building subsets incrementally.
        # At each step, an element is either included in the current subset or skipped.

        all_subsets = []
        current_subset = []
        n = len(nums)

        def backtrack(start_index):
            all_subsets.append(list(current_subset))

            for i in range(start_index, n):
                current_subset.append(nums[i])
                backtrack(i + 1)
                current_subset.pop()

        backtrack(0)
        return all_subsets