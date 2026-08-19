# Substring with Concatenation of All Words
# Difficulty: Hard
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

import collections

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        # This problem can be solved using a sliding window for each possible starting alignment.
        # Since all words have the same length, there are 'word_length' distinct alignments
        # (e.g., words starting at index 0, 1, 2, ..., up to word_length-1).
        # For each alignment, we maintain a window of 'num_words' words, tracking counts
        # with hash maps and sliding the window.

        if not s or not words:
            return []

        word_length = len(words[0])
        num_words = len(