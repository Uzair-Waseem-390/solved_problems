# Minimum Moves to Clean the Classroom
# Difficulty: Medium
# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

# This problem is a shortest path on a grid with varying states (position, collected litter, energy).
# BFS is suitable, and since energy can be restored, we need to store the maximum energy
# achieved for a given (position, collected_litter_mask) state to prune redundant paths.

import collections

class Solution:
    def minimumMoves(self, classroom: list[str], energy: int) -> int:
        rows = len(classroom)
        cols = len(classroom[0])
        
        start_row, start_col = -1, -1
        litter_locations = []
        
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c]