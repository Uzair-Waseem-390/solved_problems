# Lexicographically Smallest Palindromic Permutation Greater Than Target
# Difficulty: Hard
# https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

import collections

class Solution:
    def lexicographicallySmallestPalindromicPermutationGreaterTarget(self, s: str, target: str) -> str:
        # Construct the first half of the palindrome using available characters.
        # Iterate through prefix lengths matching target, then at the first differing
        # position, pick the smallest character greater than target's character.
        # If no such character exists, backtrack.
        # If a prefix is already greater, fill the rest greedily with smallest chars.

        n = len(s)
        
        # 1. Count character frequencies and determine the potential middle character
        char_counts = collections.Counter(s)
        
        middle_char = ''
        for char_