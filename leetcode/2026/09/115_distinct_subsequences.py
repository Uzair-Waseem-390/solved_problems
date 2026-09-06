# Distinct Subsequences
# Difficulty: Hard
# https://leetcode.com/problems/distinct-subsequences/

# Dynamic programming approach: dp[j] stores the number of ways to form t[0...j-1] using a prefix of s.
# Iterate through s, and for each character, update dp by iterating backwards through t.
# If s_char == t_char, dp[j] += dp[j-1] (match s_char with t_char, or don't use s_char).
# If s_char != t_char, dp[j] remains dp[j] (don't use s_char).

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s = len(s)
        len_t = len(t