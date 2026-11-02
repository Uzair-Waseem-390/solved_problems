# Triangle
# Difficulty: Medium
# https://leetcode.com/problems/triangle/

# Dynamic programming, iterating from the bottom up. We can optimize space by noticing that each row only depends on the row below it.
# So, we can use a single array to store the minimum sums for the current row, effectively using O(N) space where N is the number of rows.
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        num_rows = len(triangle)
        if num_rows == 0:
            return 0

        min_path_sums = list(triangle[num_rows - 1])

        for r in range(num_rows - 2, -1, -1):
            for i in range(len(triangle[r])):
                min_path_sums[i] = triangle[r][i] + min(min_path_sums[i], min_path_sums[i+1])
        
        return min_path_sums[0]