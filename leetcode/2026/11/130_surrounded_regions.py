# Surrounded Regions
# Difficulty: Medium
# https://leetcode.com/problems/surrounded-regions/

# The core idea is to identify 'O's that are NOT surrounded.
# These are 'O's connected to the board's edge.
# We use BFS starting from all 'O's on the border, marking them with a temporary character (e.g., '#').
# Finally, all remaining 'O's are surrounded and become 'X', and the temporary '#'s revert to 'O'.
import collections

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return

        def bfs(start_row, start_col):
            q = collections.deque([(start_row, start_col)])
            board[start_row][start_col] = '#'

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    next_r, next_c = r + dr, c + dc

                    if 0 <= next_r < m and 0 <= next_c < n and board[next_r][next_c] == 'O':
                        board[next_r][next_c] = '#'
                        q.append((next_r, next_c))

        for j in range(n):
            if board[0][j] == 'O':
                bfs(0, j)
            if board[m - 1][j] == 'O':
                bfs(m - 1, j)

        for i in range(m):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][n - 1] == 'O':
                bfs(i, n - 1)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'