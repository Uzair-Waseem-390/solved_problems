# Letter Combinations of a Phone Number
# Difficulty: Medium
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Backtracking is a natural fit for generating all combinations.
# We map digits to letters and recursively build combinations by iterating through letters for each digit.

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result_combinations = []
        
        def backtrack(index, current_combination):
            if index == len(digits):
                result_combinations.append(current_combination)
                return

            current_digit = digits[index]
            possible_letters = digit_to_letters[current_digit]

            for char_from_digit in possible_letters:
                backtrack(index + 1, current_combination + char_from_digit)

        backtrack(0, "")
        return result_combinations