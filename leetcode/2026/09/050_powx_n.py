# Pow(x, n)
# Difficulty: Medium
# https://leetcode.com/problems/powx-n/

# Uses iterative binary exponentiation (exponentiation by squaring) for O(log n) time complexity.
# Handles negative exponents by calculating for the positive exponent and then taking the reciprocal.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        is_n_negative = False
        if n < 0:
            is_n_negative = True
            n = -n
        
        power_result = 1.0
        base_val = x

        while n > 0:
            if n % 2 == 1:
                power_result *= base_val
            
            base_val *= base_val
            n //= 2

        if is_n_negative:
            return 1.0 / power_result
        else:
            return power_result