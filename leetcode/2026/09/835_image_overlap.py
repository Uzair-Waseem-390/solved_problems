# Image Overlap
# Difficulty: Medium
# https://leetcode.com/problems/image-overlap/

# Iterate through all possible relative shifts between the two images.
# For each shift (dx, dy), calculate the overlap by checking corresponding cells.
# The maximum overlap found across all shifts is the result.
class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        for dy in range(-(n - 1), n):
            for dx in range(-(n - 1), n):
                current_overlap = 0
                
                for r in range(n):
                    for c in range(n):
                        if img2[r][c] == 1:
                            prev_r = r - dy
                            prev_c = c - dx

                            if 0 <= prev_r < n and 0 <= prev_c < n and img1[prev_r][prev_c] ==