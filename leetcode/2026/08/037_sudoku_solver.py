# Sudoku Solver
# Difficulty: Hard
# https://leetcode.com/problems/sudoku-solver/

# Backtracking with pre-calculated row, column, and sub-box constraints using hash maps for O(1) validation.
# Iterating only through empty cells improves performance.

import collections

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [collections.defaultdict(int) for _ in range(9)]
        cols = [collections.defaultdict(int) for _ in range(9)]
        boxes = [collections.defaultdict(int) for _ in range(9)]

        empty_cells = []

        for r in range(9):
            for c in range(9):
                char_digit = board[r][c]
                if char_digit != '.':
                    rows[r][char_digit] += 1
                    cols[c][char_digit] += 1
                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index][char_digit] += 1
                else:
                    empty_cells.append((r, c))

        def backtrack(empty_cell_index):
            if empty_cell_index == len(empty_cells):
                return True

            r, c = empty_cells[empty_cell_index]
            box_index = (r // 3) * 3 + (c // 3)

            for digit_char in "123456789":
                if rows[r][digit_char] == 0 and \
                   cols[c][digit_char] == 0 and \
                   boxes[box_index][digit_char] == 0:

                    board[r][c] = digit_char
                    rows[r][digit_char] += 1
                    cols[c][digit_char] += 1
                    boxes[box_index][digit_char] += 1

                    if backtrack(empty_cell_index + 1):
                        return True

                    rows[r][digit_char] -= 1
                    cols[c][digit_char] -= 1
                    boxes[box_index][digit_char] -= 1
                    board[r][c] = '.'

            return False

        backtrack(0)