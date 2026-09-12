# N-Queens II
# Difficulty: Hard
# https://leetcode.com/problems/n-queens-ii/

# Classic backtracking problem. Use sets to efficiently check for column and diagonal conflicts.
# Iterate row by row, trying to place a queen in each column.
# If a placement is valid, mark the column and diagonals as occupied and recurse for the next row.
# After the recursive call returns, backtrack by unmarking the column and diagonals.

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.board_size = n
        self.total_solutions = 0

        # Sets to keep track of occupied columns and diagonals
        self.occupied_cols = set()
        self.occupied_diagonals_sum = set()  # For r + c
        self.occupied_diagonals_diff = set() # For r - c

        self._backtrack_solve(0)
        return self.total_solutions

    def _backtrack_solve(self, current_row: int):
        # Base case: If all queens have been successfully placed (current_row reaches n)
        if current_row == self.board_size:
            self.total_solutions += 1
            return

        # Try placing a queen in each column of the current_row
        for current_col in range(self.board_size):
            # Check if placing a queen at (current_row, current_col) is safe
            # A queen is attacked if it shares a column, or either of the two diagonals
            if (current_col in self.occupied_cols or
                (current_row + current_col) in self.occupied_diagonals_sum or
                (current_row - current_col) in self.occupied_diagonals_diff):
                continue # This position is attacked, try the next column

            # Place the queen: mark the column and diagonals as occupied
            self.occupied_cols.add(current_col)
            self.occupied_diagonals_sum.add(current_row + current_col)
            self.occupied_diagonals_diff.add(current_row - current_col)

            # Recurse for the next row
            self._backtrack_solve(current_row + 1)

            # Backtrack: Remove the queen (undo the placement)
            self.occupied_cols.remove(current_col)
            self.occupied_diagonals_sum.remove(current_row + current_col)
            self.occupied_diagonals_diff.remove(current_row - current_col)