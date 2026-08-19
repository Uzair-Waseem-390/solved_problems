# Divide Two Integers
# Difficulty: Medium
# https://leetcode.com/problems/divide-two-integers/

# Bit manipulation is key here, essentially implementing division as repeated subtraction of powers of two of the divisor.
# Handle signs and 32-bit integer overflow limits at the start and end.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        is_negative = (dividend < 0) != (divisor < 0)

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        quotient = 0

        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            temp_quotient = 1
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                temp_quotient <<= 1
            
            abs_dividend -= temp_divisor
            quotient += temp_quotient
        
        if is_negative:
            quotient = -quotient
        
        if quotient > INT_MAX:
            return INT_MAX
        if quotient < INT_MIN:
            return INT_MIN
        
        return quotient