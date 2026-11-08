# Word Ladder
# Difficulty: Hard
# https://leetcode.com/problems/word-ladder/

import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Use BFS to find the shortest path. Pre-process wordList into a graph
        # where keys are generic patterns (e.g., "h*t") and values are words
        # matching that pattern, enabling efficient neighbor lookup.

        if endWord not in wordList:
            return 0

        word_length = len(beginWord)
        
        # Dictionary to store all possible patterns and the words that match them.
        # E.g., {"h*t": ["hot", "hat"], "*ot": ["hot", "dot"], ...}
        pattern