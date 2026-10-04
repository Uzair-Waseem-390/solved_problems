# Combinations
# Difficulty: Medium
# https://leetcode.com/problems/combinations/

# Classic backtracking problem. A recursive helper function builds combinations by choosing numbers
# sequentially and exploring branches. Pruning significantly optimizes by limiting the search space.
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        all_combinations = []
        current_combination = []

        def backtrack(start_number):
            if len(current_combination) == k:
                all_combinations.append(list(current_combination))
                return

            upper_bound_for_selection = n - (k - len(current_combination)) + 1

            for num_to_add in range(start_number, upper_bound_for_selection + 1):
                current_