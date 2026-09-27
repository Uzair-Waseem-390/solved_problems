# Unique Paths
# Difficulty: Medium
# https://leetcode.com/problems/unique-paths/

# This problem can be solved using combinatorics, as the robot must make a fixed number of down and right moves in any order.
# The total number of moves is (m-1) + (n-1), and we need to choose (m-1) of them to be down moves (or (n-1) to be right moves).
# This is equivalent to C(m+n-2, m-1) or C(m+n-2, n-1).

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        # Total number of steps required is (m-1) down moves