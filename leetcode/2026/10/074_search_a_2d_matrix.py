# Search a 2D Matrix
# Difficulty: Medium
# https://leetcode.com/problems/search-a-2d-matrix/

# The matrix properties (sorted rows, first element of row > last of previous)
# allow treating it as a single sorted 1D array.
# A binary search on this virtual 1D array gives O(log(m*n)) time complexity.
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        low_index = 0
        high_index = rows * cols - 1

        while low_index <= high_index:
            mid_index = low_index + (high_index - low_index) // 2
            
            current_row = mid_index // cols
            current_col = mid_index % cols
            
            middle_value = matrix[current_row][current_col]

            if middle_value == target:
                return True
            elif middle_value < target:
                low_index = mid_index + 1
            else:
                high_index = mid_index - 1
        
        return False