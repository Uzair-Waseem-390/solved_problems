# Max Points on a Line
# Difficulty: Hard
# https://leetcode.com/problems/max-points-on-a-line/

# Iterate through each point as a pivot. For each pivot, calculate slopes to all subsequent points.
# Store slopes as simplified fractions (dy/dx) in a hash map to count points on the same line.
# The greatest common divisor (GCD) helps simplify fractions and handles vertical/horizontal lines canonically.

import math

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        num_points = len(points)
        if num_points <= 2:
            return num_points

        max_points_on_line = 0

        for i in range(num_points):
            current_point = points[i]
            slopes_count = {}
            current_max