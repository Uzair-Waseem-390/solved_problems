# Distinct Subsequences II
# Difficulty: Hard
# https://leetcode.com/problems/distinct-subsequences-ii/

# Dynamic programming approach. dp[i] represents total distinct non-empty subsequences for s[0...i-1].
# When processing s[i-1], we double the previous count (2 * dp[i-1]) for new subsequences (s[i-1] itself + s[i-1] appended to all previous).
# If s[i-1] has appeared before, we subtract the count of subsequences that ended with its previous occurrence to avoid duplicates.
# A `last_occurrence_count` array helps track the count of subsequences ending with each character at its most recent prior appearance.

class Solution:
    def distinctSubsequencesII(self, s: str) -> int:
        MOD = 10**9