# Minimum Element After Replacement With Digit Sum
# Difficulty: Easy
# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

# Iterate through each number in the array, calculate the sum of its digits, and track the minimum sum encountered.

class Solution:
    def minimumElementAfterReplacement(self, nums: list[int]) -> int:
        min_val_after_replacement = float('inf')

        for current_number in nums:
            sum_of_digits = 0
            temp_num = current_number
            
            while temp_num > 0:
                digit = temp_num % 10
                sum_of_digits += digit
                temp_num //= 10
            
            min_val_after_replacement = min(min_val_after_replacement, sum_of_digits)
        
        return min_val_after_replacement