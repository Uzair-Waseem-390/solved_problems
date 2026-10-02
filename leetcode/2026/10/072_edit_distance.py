# Edit Distance
# Difficulty: Medium
# https://leetcode.com/problems/edit-distance/

# Classic dynamic programming problem.
# Define dp[i][j] as the minimum edit distance between word1[:i] and word2[:j].
# Base cases handle empty strings, and transitions consider insert, delete, or replace,
# or no operation if characters match.
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            dp[i][0] = i
        
        for j in range(len