# Gray Code
# Difficulty: Medium
# https://leetcode.com/problems/gray-code/

# The standard Gray code sequence can be generated directly using the formula G(i) = i ^ (i >> 1)
# for i ranging from 0 to 2^n - 1. This formula efficiently produces a valid sequence where adjacent numbers differ by one bit.
class Solution:
    def grayCode(self, n: int) -> list[int]:
        
        number_of_elements = 1 << n
        gray_code_sequence = []
        
        for i in range(number_of_elements):
            gray_code_sequence.append(i ^ (i >> 1))
            
        return gray_code_sequence