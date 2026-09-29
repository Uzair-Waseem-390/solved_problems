# Valid Number
# Difficulty: Hard
# https://leetcode.com/problems/valid-number/

# This problem is a classic string parsing task best handled by breaking it down into sub-problems and using helper functions
# to validate each part (digits, integer, decimal, exponent). The main function orchestrates these checks.

class Solution:
    def isNumber(self, s: str) -> bool:

        def is_digits(part: str) -> bool:
            if not part:
                return False
            for char in part:
                if not char.isdigit():
                    return False
            return True

        def is_integer_part(part: str) -> bool:
            if not part:
                return False
            start_index = 0
            if part[0] == '+' or part[0] == '-':