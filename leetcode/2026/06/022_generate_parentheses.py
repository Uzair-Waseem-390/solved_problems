# Generate Parentheses
# Difficulty: Medium
# https://leetcode.com/problems/generate-parentheses/

# This is a classic backtracking problem where we explore all possibilities by adding '(' or ')'
# at each step, subject to rules to maintain well-formed parentheses (e.g., cannot close before opening, cannot exceed total n pairs).

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result_combinations = []

        def backtrack(current_string_builder: list[str], num_open_placed: int, num_close_placed: int):
            if num_open_placed == n and num_close_placed == n:
                result_combinations.append("".join(current_string_builder))
                return

            if num_open_placed < n:
                current_string_builder.append('(')
                backtrack(current_string_builder, num_open_placed + 1, num_close_placed)
                current_string_builder.pop()

            if num_close_placed < num_open_placed:
                current_string_builder.append(')')
                backtrack(current_string_builder, num_open_placed, num_close_placed + 1)
                current_string_builder.pop()

        backtrack([], 0, 0)
        return result_combinations