# Unique Paths II
# Difficulty: Medium
# https://leetcode.com/problems/unique-paths-ii/

# Dynamic programming approach.
# dp[i][j] stores the number of unique paths to reach cell (i, j).
# If a cell is an obstacle, it has 0 paths. Otherwise, paths to (i, j)
# are the sum of paths from (i-1, j) and (i, j-1).
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        path_counts = [[0] * cols for _ in range(rows)]

        path_counts[