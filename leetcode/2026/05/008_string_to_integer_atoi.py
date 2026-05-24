# String to Integer (atoi)
# Difficulty: Medium
# https://leetcode.com/problems/string-to-integer-atoi/

# Follows the problem's step-by-step algorithm: handle leading whitespace, determine sign,
# then iterate through digits while building the number and performing overflow checks against INT_MAX/INT_MIN.

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        string_length = len(s)
        current_index = 0
        current_sign = 1
        result_number = 0

        while current_index < string_length and s[current_index] == ' ':
            current_index += 1

        if current_index < string_length:
            if s[current_index] == '-':
                current_sign = -1
                current_index += 1
            elif s[current_index] == '+':
                current_index += 1

        while current_index < string_length and s[current_index].isdigit():
            digit = int(s[current_index])

            if result_number > INT_MAX // 10 or \
               (result_number == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if current_sign == 1 else INT_MIN
            
            result_number = result_number * 10 + digit
            current_index += 1
        
        return result_number * current_sign