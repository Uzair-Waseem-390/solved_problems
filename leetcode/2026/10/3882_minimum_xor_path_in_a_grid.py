# Minimum XOR Path in a Grid
# Difficulty: Medium
# https://leetcode.com/problems/minimum-xor-path-in-a-grid/

# DP with boolean array to track reachable XOR sums. Max XOR value is 1023, so a boolean array of size 1024 is feasible for each cell.
# The total number of cells m*n is small (<= 1000), making m*n*1024 operations acceptable.

class Solution:
    def minimumXORPath(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        MAX_POSSIBLE_XOR_VALUE = 1024

        dp_reachable_xors = [[[False] * MAX_POSSIBLE_XOR_VALUE for _ in range(cols)] for _ in