# Container With Most Water
# Difficulty: Medium
# https://leetcode.com/problems/container-with-most-water/

# This problem can be efficiently solved using a two-pointer approach.
# Start with pointers at both ends of the array and calculate the area.
# To maximize the area, always move the pointer associated with the shorter line inwards,
# as moving the taller line's pointer would only decrease width without a guaranteed increase in height.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer < right_pointer:
            current_width = right_pointer - left_pointer
            current_height = min(height[left_pointer], height[right_pointer])
            current_area = current_height * current_width
            max_water = max(max_water, current_area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return max_water