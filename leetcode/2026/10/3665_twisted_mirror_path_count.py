# Twisted Mirror Path Count
# Difficulty: Medium
# https://leetcode.com/problems/twisted-mirror-path-count/

class Solution:
    def solve(self, r, c, entry_direction):
        # Memoization key: (row, col, direction of entry)
        # entry_direction: 0 if entered (r,c) from left (moving right), 1 if entered (r,c) from above (moving down)
        key = (r, c, entry_direction)
        if key in self.memo:
            return self.memo[key]

        # Check if current cell is out of bounds
        if not (0 <= r < self.m and 0 <= c < self.n):
            self.memo[key] = (-1, -1)
            return (-1, -1)

        # If