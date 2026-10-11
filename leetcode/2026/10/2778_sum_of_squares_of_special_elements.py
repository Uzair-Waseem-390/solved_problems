# Sum of Squares of Special Elements 
# Difficulty: Easy
# https://leetcode.com/problems/sum-of-squares-of-special-elements/

# Simple iteration over 1-indexed positions, checking divisibility for the special condition, and summing squares.

class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        array_length = len(nums)
        total_sum_of_squares = 0

        for i in range(1, array_length + 1):
            if array_length % i == 0:
                total_sum_of_squares += nums[i - 1] * nums[i - 1]
        
        return total_sum_of_squares