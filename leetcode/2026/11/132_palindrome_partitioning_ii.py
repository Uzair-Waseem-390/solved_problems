# Palindrome Partitioning II
# Difficulty: Hard
# https://leetcode.com/problems/palindrome-partitioning-ii/

# This problem can be solved using dynamic programming.
# First, precompute all possible palindromic substrings using a 2D boolean DP table.
# Then, use another 1D DP table to find the minimum cuts.
# dp[i] represents the minimum cuts needed for the prefix s[0...i].

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # is_palindrome[i][j] will be True if s[i...j] is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]

        # Populate is_palindrome table
        # Iterate by gap (length-1)
        for gap in range(n