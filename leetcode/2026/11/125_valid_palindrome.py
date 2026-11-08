# Valid Palindrome
# Difficulty: Easy
# https://leetcode.com/problems/valid-palindrome/

# Two-pointer approach is suitable here. We iterate inwards from both ends,
# skipping non-alphanumeric characters, and compare lowercase versions of
# the alphanumeric characters.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            while left_pointer < right_pointer and not s[left_pointer].isalnum():
                left_pointer += 1
            while left_pointer < right_pointer and not s[right_pointer].isalnum():
                right_pointer -= 1

            if left_pointer < right_pointer:
                if s[left_pointer].lower() != s[right_pointer].lower():
                    return False
                left_pointer += 1
                right_pointer -= 1
        
        return True