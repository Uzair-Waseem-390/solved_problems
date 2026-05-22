# Longest Palindromic Substring
# Difficulty: Medium
# https://leetcode.com/problems/longest-palindromic-substring/

# The "expand around center" approach works well here. Iterate through each character as a potential center for odd-length palindromes, and between each pair of characters for even-length palindromes. Expand outwards to find the longest palindrome from each center.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        string_length = len(s)
        if string_length < 2:
            return s

        longest_palindrome_start = 0
        longest_palindrome_length = 0

        def expand_around_center(left_pointer: int, right_pointer: int) -> int:
            while left_pointer >= 0 and right_pointer < string_length and s[left_pointer] == s[right_pointer]:
                left_pointer -= 1
                right_pointer += 1
            return right_pointer - left_pointer - 1

        for i in range(string_length):
            # Odd length palindromes, centered at s[i]
            length_odd_center = expand_around_center(i, i)
            # Even length palindromes, centered between s[i] and s[i+1]
            length_even_center = expand_around_center(i, i + 1)

            current_max_length = max(length_odd_center, length_even_center)

            if current_max_length > longest_palindrome_length:
                longest_palindrome_length = current_max_length
                # Calculate the start index: current_center - (length - 1) / 2
                longest_palindrome_start = i - (current_max_length - 1) // 2

        return s[longest_palindrome_start : longest_palindrome_start + longest_palindrome_length]