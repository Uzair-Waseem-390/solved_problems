# Longest Subsequence With Non-Zero Bitwise XOR
# Difficulty: Medium
# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

# The longest subsequence is either the entire array (if its XOR sum is non-zero) or the entire array minus one element (if the total XOR sum is zero but there's a non-zero element to remove). If all elements are zero, no such subsequence exists.

class Solution:
    def longestSubsequenceWithNonZeroXOR(self, nums: list[int]) -> int:
        array_length = len(nums)
        
        total_xor_sum = 0
        contains_non_zero = False
        
        for num in nums:
            total_xor_sum ^= num
            if num != 0:
                contains_non_zero = True
        
        if total_xor_sum != 0:
            return array_length
        else:
            if contains_non_zero:
                return array_length - 1
            else:
                return 0