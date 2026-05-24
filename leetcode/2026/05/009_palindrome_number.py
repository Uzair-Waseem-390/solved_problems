# Palindrome Number
# Difficulty: Easy
# https://leetcode.com/problems/palindrome-number/

# Handle negative numbers and numbers ending in zero (except 0 itself) as non-palindromes.
# Then, reverse the second half of the number and compare it with the first half.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # When the number has an odd number of digits, x will be the middle digit
        # and reversed_half will have one more digit than x.
        # We can remove the middle digit from reversed_half by dividing by 10.
        return x == reversed_half or x == reversed_half // 10