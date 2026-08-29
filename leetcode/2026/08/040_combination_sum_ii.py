# Combination Sum II
# Difficulty: Medium
# https://leetcode.com/problems/combination-sum-ii/

# Backtracking with sorting and a skip condition to handle duplicate numbers and ensure unique combinations.
# Each number can only be used once in a combination, so the recursion moves to the next index (i+1).

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        candidates.sort()

        def backtrack(current_combination, remaining_target, start_index):
            if remaining_target == 0:
                results.append(list(current_combination))
                return
            if remaining_target < 0:
                return

            for i in range(start_index, len(candidates)):
                if i > start_index and