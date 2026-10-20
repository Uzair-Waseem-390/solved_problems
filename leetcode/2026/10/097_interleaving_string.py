# Interleaving String
# Difficulty: Medium
# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len1 + len2 != len3:
            return False

        # dp[j] will store whether s1[:i] and s2[:j] can interleave to form s3[:i+j]
        # We optimize space by using only the current and previous row.
        # current_row[j] corresponds to dp[i][j]
        # previous_row[j] corresponds to dp[i-1][j]