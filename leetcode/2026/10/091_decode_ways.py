# Decode Ways
# Difficulty: Medium
# https://leetcode.com/problems/decode-ways/

# Dynamic programming approach: `dp[i]` stores the number of ways to decode `s[i:]`.
# We iterate backwards, calculating `dp[i]` based on single-digit and two-digit decoding possibilities.
# Base cases handle empty string (1 way) and invalid leading zeros (0 ways).

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        # dp[i] will store the number of ways to decode the substring s[i:]
        # dp array size n+1 to handle the base case for an empty string
        dp = [0] * (n + 1)
        
        # Base case: An empty string (