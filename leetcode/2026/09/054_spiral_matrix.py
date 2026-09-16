# Spiral Matrix
# Difficulty: Medium
# https://leetcode.com/problems/spiral-matrix/

# Simulate the spiral traversal layer by layer, adjusting boundary pointers (top, bottom, left, right) after each direction.
# Crucial to check boundary conditions (e.g., top_row <= bottom_row) after each traversal to prevent processing empty layers or duplicate elements.

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        rows = len(matrix)
        cols = len(matrix[0])

        top_row = 0
        bottom_row = rows - 1
        left_col = 0
        right_col = cols - 1

        while top_row <= bottom_row and left_col <= right_col:
            # Traverse right along the top row
            for col in range(left_col, right_col + 1):
                result.append(matrix[top_row][col])
            top_row += 1
            if top_row > bottom_row:
                break

            # Traverse down along the right column
            for row in range(top_row, bottom_row + 1):
                result.append(matrix[row][right_col])
            right_col -= 1
            if left_col > right_col:
                break

            # Traverse left along the bottom row
            for col in range(right_col, left_col - 1, -1):
                result.append(matrix[bottom_row][col])
            bottom_row -= 1
            if top_row > bottom_row:
                break

            # Traverse up along the left column
            for row in range(bottom_row, top_row - 1, -1):
                result.append(matrix[row][left_col])
            left_col += 1
            if left_col > right_col:
                break

        return result