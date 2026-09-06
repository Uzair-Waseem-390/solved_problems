# Wildcard Matching
# Difficulty: Hard
# https://leetcode.com/problems/wildcard-matching/

# Dynamic programming approach where dp[i][j] indicates if s[:i] matches p[:j].
# The '*' character can match an empty sequence (dp[i][j-1]) or one or more characters (dp[i-1][j]).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]

        dp[0][0] = True

        for j in range(1, p_len + 1):
            if p[j-1] == '*':