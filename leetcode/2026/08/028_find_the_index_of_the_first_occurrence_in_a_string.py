# Find the Index of the First Occurrence in a String
# Difficulty: Easy
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# Naive string search approach using slicing. Iterate through haystack and compare substrings with needle.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        # Iterate through all possible starting positions for needle in haystack
        # The loop runs from index 0 up to n - m
        # If n - m + 1 is less than or equal to 0 (e.g., needle is longer than haystack),
        # the range will be empty, and the loop won't execute, correctly returning -1.
        for i in range(n - m + 1):
            # Check if the substring of haystack starting at i with length m matches needle
            if haystack[i : i + m] == needle:
                return i
        
        # If the loop completes without finding a match, needle is not in haystack
        return -1