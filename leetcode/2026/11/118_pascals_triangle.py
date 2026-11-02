# Pascal's Triangle
# Difficulty: Easy
# https://leetcode.com/problems/pascals-triangle/

# Dynamic programming approach: each row is built from the previous row by summing adjacent elements.
# Start with the first row [1], then iterate to build subsequent rows.

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal_triangle = []

        if numRows >= 1:
            pascal_triangle.append([1])

        for row_index in range(1, numRows):
            previous_row = pascal_triangle[row_index - 1]
            current_row = [1] 

            for j in range(len(previous_row) - 1):
                current_row.append(previous_row[j] + previous_row[j+1])
            
            current_row.append(1)
            pascal_triangle.append(current_row)

        return pascal_triangle