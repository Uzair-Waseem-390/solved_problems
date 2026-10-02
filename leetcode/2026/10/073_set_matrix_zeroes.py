# Set Matrix Zeroes
# Difficulty: Medium
# https://leetcode.com/problems/set-matrix-zeroes/

# This problem can be solved in O(1) space by using the first row and first column of the matrix
# itself to store the zero-state markers. A separate boolean is needed to track the state of
# the very first column due to the ambiguity of matrix[0][0] serving as both a row and column marker.

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Use a boolean to track if the first column needs to be zeroed
        # This is needed because matrix[0][0] can be used as a marker for both
        # the first row and the first