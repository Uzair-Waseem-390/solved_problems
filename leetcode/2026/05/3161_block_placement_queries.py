# Block Placement Queries
# Difficulty: Hard
# https://leetcode.com/problems/block-placement-queries/

# Uses a segment tree with lazy propagation to efficiently handle range updates (placing obstacles) and range maximum queries (checking block placement).
# Each node stores the maximum free space ending within its range. Updates involve setting free space relative to the new obstacle.

import collections

class Solution:
    def blockPlacementQueries(self, queries: list[list[int]]) -> list[bool]:
        # Coordinate compression isn't strictly necessary given MAX_COORD, but good practice
        # for segment tree problems where coordinates can be sparse.
        # Here, MAX_COORD is small enough that a direct segment tree is fine.
        # Max coordinate is min(5 * 10^4, 3 * queries.length).
        # max_x_val is the