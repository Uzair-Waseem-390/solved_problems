# Valid Sudoku
# Difficulty: Medium
# https://leetcode.com/problems/valid-sudoku/

# Use three sets (for rows, columns, and 3x3 sub-boxes) to track seen numbers.
# Iterate through the board once, adding numbers to the respective sets and checking for duplicates.

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                current_char = board[r][c]
                if current_char == '.':
                    continue

                if current_char in rows[r]:
                    return False
                rows[r].add(current_char)

                if current_char in cols[c]:
                    return False
                cols[c].add(current_char)

                box_index = (r // 3) * 3 + (c // 3)
                if current_char in boxes[box_index]:
                    return False
                boxes[box_index].add(current_char)
        
        return True