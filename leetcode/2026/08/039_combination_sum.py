# Combination Sum
# Difficulty: Medium
# https://leetcode.com/problems/combination-sum/

# This problem is a classic backtracking scenario. We need to explore all possible combinations
# where numbers can be reused. The key is to pass the current index to the recursive call
# to allow re-selection of the same number while avoiding duplicate combinations due to order.

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        all_combinations = []
        current_combination = []

        def backtrack(remaining_target: int, start_index: int):
            if remaining_target == 0:
                all_combinations.append(list(current_combination))
                return

            if remaining_target < 0:
                return

            for i in range(start_index, len(candidates)):
                candidate_value = candidates[i]
                current_combination.append(candidate_value)
                backtrack(remaining_target - candidate_value, i)
                current_combination.pop()

        backtrack(target, 0)
        return all_combinations