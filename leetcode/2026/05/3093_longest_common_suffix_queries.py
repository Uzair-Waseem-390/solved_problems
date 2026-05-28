# Longest Common Suffix Queries
# Difficulty: Hard
# https://leetcode.com/problems/longest-common-suffix-queries/

# Reversing strings and using a Trie to find the longest common prefix (which is the longest common suffix in original strings).
# Each Trie node stores the (length, original_index) of the best word passing through it,
# prioritizing shortest length then smallest original index.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_candidate = (float('inf'), float('inf')) # (length, original_index)

class Solution:
    def longestCommonSuffixQueries(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        root = TrieNode()

        for i, word in enumerate(wordsContainer):
            current_node = root
            original