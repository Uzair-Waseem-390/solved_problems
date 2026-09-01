# Trapping Rain Water
# Difficulty: Hard
# https://leetcode.com/problems/trapping-rain-water/

# The two-pointer approach efficiently calculates trapped water by maintaining
# maximum heights from both ends and moving the pointer associated with the smaller height.
# This ensures that the limiting wall for water calculation is always known.
class Solution:
    def trap(self, height: list[int]) -> int:
        num_bars = len(height)
        if num_bars < 3:
            return 0

        left_pointer = 0
        right_pointer = num_bars - 1
        
        max_left_height = 0
        max_right_height = 0
        
        total_trapped_water = 0

        while left_pointer <= right_pointer:
            if height[left_pointer]