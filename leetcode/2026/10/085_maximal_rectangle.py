# Maximal Rectangle
# Difficulty: Hard
# https://leetcode.com/problems/maximal-rectangle/

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        # This problem can be reduced to finding the largest rectangle in a histogram for each row.
        # Iterate through rows, maintaining a `heights` array that represents the histogram of consecutive '1's above the current row.
        # For each row, update the `heights` array and then apply the standard "Largest Rectangle in Histogram" algorithm using a monotonic stack.
        
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        
        current_heights = [0] * cols
        max_overall_area = 0