# Count Servers that Communicate
# Difficulty: Medium
# https://leetcode.com/problems/count-servers-that-communicate/

# First pass to count servers in each row and column, then second pass to count servers
# that have more than one server in their row OR more than one server in their column.
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        row_server_counts = [0] * rows
        col_server_counts = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_server_counts[r] += 1
                    col_server_counts[c] += 1

        communicating_servers = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if row_server_counts[r] > 1 or col_server_counts[c] > 1:
                        communicating_servers += 1
        
        return communicating_servers