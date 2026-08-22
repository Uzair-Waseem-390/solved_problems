# Check Divisibility by Digit Sum and Product
# Difficulty: Easy
# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

# Calculate digit sum and product by repeatedly taking modulo 10 and integer dividing by 10.
# Then check if the original number is divisible by the sum of these two calculated values.
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        
        temp_n = n
        while temp_n > 0:
            current_digit = temp_n % 10
            digit_sum += current_digit
            digit_product *= current_digit
            temp_n //= 10
            
        total_divisor = digit_sum + digit_product
        
        return n % total_divisor == 0