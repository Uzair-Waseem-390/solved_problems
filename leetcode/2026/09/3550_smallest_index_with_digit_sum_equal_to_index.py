# Smallest Index With Digit Sum Equal to Index
# Difficulty: Easy
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

# Iterate through indices, calculate digit sum for each number, and return the first matching index.
# If no match is found after checking all indices, return -1.

class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for index, current_number in enumerate(nums):
            digit_sum = 0
            temp_number = current_number
            while temp_number > 0:
                digit_sum += temp_number % 10
                temp_number //= 10
            
            # Special case for 0: sum of digits is 0.
            # The loop above correctly handles it if current_number is 0, digit_sum will remain 0.
            
            if digit_sum == index:
                return index
        
        return -1