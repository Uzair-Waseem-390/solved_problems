#  Check if There Is a Valid Parentheses String Path
# Difficulty: Hard
# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

# Dynamic programming approach where dp[r][c] stores a set of possible parenthesis balances
# at cell (r,c). Pruning conditions are applied: balance must be non-negative,
# balance must not exceed remaining path length, and balance parity must match remaining path length parity.

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        path_length = m + n - 1
        if path_length % 2 != 0:
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]

        if grid[0][0]