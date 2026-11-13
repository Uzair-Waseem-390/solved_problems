# Single Number
# Difficulty: Easy
# https://leetcode.com/problems/single-number/

# The XOR bitwise operation property (a ^ a = 0 and a ^ 0 = a) means that XORing all numbers in the array will cancel out all elements that appear twice, leaving only the unique single number. This approach ensures linear time complexity and constant extra space.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number