# Reverse Integer
# Difficulty: Medium
# https://leetcode.com/problems/reverse-integer/

# Iteratively extract digits, build the reversed number, and check for 32-bit integer overflow at each step.
# Use Python's integer division and modulo which handle signs differently than some other languages, so it's safer to work with the absolute value and then apply the sign.

class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2147483647
        min_int = -2147483648
        
        sign = 1
        if x < 0:
            sign = -1
            x = -x # Work with positive x
        
        reversed_num = 0
        
        while