# Count Islands With Total Value Divisible by K
# Difficulty: Medium
# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

# Standard DFS approach to find connected components (islands) and sum their values.
# Mark visited cells by setting their value to 0 to prevent revisiting and ensure O(1) space for visited tracking.

class Solution:
    def countDivisibleIslands(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        divisible_islands_count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            current_cell_value = grid[r][c]