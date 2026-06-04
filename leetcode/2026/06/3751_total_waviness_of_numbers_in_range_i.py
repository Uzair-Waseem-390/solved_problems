# Total Waviness of Numbers in Range I
# Difficulty: Medium
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

# Given the small constraints (up to 10^5), a straightforward brute-force approach is efficient enough.
# Iterate through each number, convert it to a string, and count peaks/valleys based on the problem definition.

class Solution:
    def _calculate_waviness_for_number(self, num: int) -> int:
        s = str(num)
        
        if len(s) < 3:
            return 0
        
        current_waviness = 0
        for i in range(1, len(s) - 1):
            left_digit = int(s[i - 1])
            current_digit = int(s[i])
            right_digit = int(s[i + 1])
            
            if current_digit > left_digit and current_digit > right_digit:
                current_waviness += 1
            elif current_digit < left_digit and current_digit < right_digit:
                current_waviness += 1
                
        return current_waviness

    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness_sum = 0
        for num in range(num1, num2 + 1):
            total_waviness_sum += self._calculate_waviness_for_number(num)
            
        return total_waviness_sum