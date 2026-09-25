# Spiral Matrix II
# Difficulty: Medium
# https://leetcode.com/problems/spiral-matrix-ii/

# Simulate filling the matrix layer by layer, expanding inwards from the boundaries.
# Keep track of current boundaries (top, bottom, left, right) and the number to fill.

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        current_number = 1
        top_bound = 0
        bottom_bound = n - 1
        left_bound = 0
        right_bound = n - 1
        
        while current_number <= n * n:
            # Traverse right across the top row
            for col in range(left_bound, right_bound + 1):
                matrix[top_bound][col] = current_number
                current_number += 1
            top_bound += 1
            
            # Traverse down the rightmost column
            for row in range(top_bound, bottom_bound + 1):
                matrix[row][right_bound] = current_number
                current_number += 1
            right_bound -= 1
            
            # Traverse left across the bottom row
            if top_bound <= bottom_bound: # Check if there's still a row to traverse
                for col in range(right_bound, left_bound - 1, -1):
                    matrix[bottom_bound][col] = current_number
                    current_number += 1
                bottom_bound -= 1
            
            # Traverse up the leftmost column
            if left_bound <= right_bound: # Check if there's still a column to traverse
                for row in range(bottom_bound, top_bound - 1, -1):
                    matrix[row][left_bound] = current_number
                    current_number += 1
                left_bound += 1
                
        return matrix