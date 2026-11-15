# Single Number II
# Difficulty: Medium
# https://leetcode.com/problems/single-number-ii/

# The core idea is to count the occurrences of each bit at every position (0 to 31).
# Since every number appears three times except one, the sum of bits at any position,
# when taken modulo 3, will reveal the corresponding bit of the single number.
# Special handling is needed for negative numbers to convert the final 32-bit unsigned
# representation back to a signed integer.
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single_number = 0
        
        for i in range(32):
            bit_sum = 0
            for num in nums:
                bit = (num >> i) & 1
                bit_sum += bit