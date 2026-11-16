# Word Break
# Difficulty: Medium
# https://leetcode.com/problems/word-break/

# Dynamic programming approach. `dp[i]` is true if `s[0:i]` can be segmented.
# Iterate through all possible end points `i` and then all possible start points `j` for a word `s[j:i]`.
# If `dp[j]` is true and `s[j:i]` is in the dictionary, then `dp[i]` is true.
# Using a set for `wordDict` allows for efficient word lookups.

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        string_length = len(s)
        
        dp = [False] * (string_length + 1)
        dp[0] = True