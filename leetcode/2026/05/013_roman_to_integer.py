# Roman to Integer
# Difficulty: Easy
# https://leetcode.com/problems/roman-to-integer/

# Iterate through the Roman numeral string from right to left.
# If the current symbol's value is less than the previous symbol's value (from the right), subtract it; otherwise, add it.
# This handles the subtractive rules (IV, IX, XL, etc.) naturally.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total_integer_value = 0
        previous_symbol_value = 0

        for char_roman in reversed(s):
            current_symbol_value = roman_map[char_roman]

            if current_symbol_value < previous_symbol_value:
                total_integer_value -= current_symbol_value
            else:
                total_integer_value += current_symbol_value
            
            previous_symbol_value = current_symbol_value
        
        return total_integer_value