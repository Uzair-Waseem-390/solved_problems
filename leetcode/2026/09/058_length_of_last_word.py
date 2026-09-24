# Length of Last Word
# Difficulty: Easy
# https://leetcode.com/problems/length-of-last-word/

# Using Python's split() method is the most straightforward and Pythonic way to handle words and spaces.
# The default split behavior correctly handles multiple spaces and leading/trailing spaces.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        last_word = words[-1]
        return len(last_word)