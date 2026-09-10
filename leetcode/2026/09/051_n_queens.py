# N-Queens
# Difficulty: Hard
# https://leetcode.com/problems/n-queens/

# Backtracking with sets for O(1) conflict checks (columns, diagonals) is efficient.
# Iteratively place queens row by row, checking safety with sets, and backtrack if no solution found from a position.

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        solutions = []
        
        # Keep track of occupied columns, main diagonals (row - col), and anti-diagonals (row + col)
        cols_occupied = set()
        diag1_occupied = set()  # row - col
        diag2_occupied = set()  # row + col

        # current_queen_placements stores the column index for the queen in each row.
        # e