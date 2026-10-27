# Create Grid With Exactly One Path
# Difficulty: Easy
# https://leetcode.com/problems/create-grid-with-exactly-one-path/

# The strategy is to define a simple path and make all other cells obstacles.
# A straightforward path is to go right all the way to (0, n-1), then down all the way to (m-1, n-1).
# This ensures that at each step of the path, there is only one valid next free cell to move to.

class Solution:
    def createGridWithExactlyOnePath(self, m: int, n: int) -> list[str]:
        grid = [['#' for _ in range(n)] for _ in range(m)]

        # Path segment 1: Go right from (0,0) to (0, n-1)
        for j in range(n):
            grid[