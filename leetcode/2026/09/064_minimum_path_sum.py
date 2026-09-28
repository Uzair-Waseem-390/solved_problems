# Minimum Path Sum
# Difficulty: Medium
# https://leetcode.com/problems/minimum-path-sum/

# Dynamic programming approach where the grid itself is used to store minimum path sums to reach each cell.
# The value at grid[i][j] will represent the minimum sum to reach (i,j) from (0,0).

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue  # Starting cell, no path sum to add
                elif r == 0:
                    grid[r][c] += grid[r][c-1]  # Only move right in the first row
                elif c == 0:
                    grid[r][c] += grid[r-1][c]  # Only move down in the first column
                else:
                    # Can come from above (r-1, c) or from left (r, c-1)
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        
        return grid[rows-1][cols-1]