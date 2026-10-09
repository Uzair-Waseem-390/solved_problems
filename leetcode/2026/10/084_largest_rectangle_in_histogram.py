# Largest Rectangle in Histogram
# Difficulty: Hard
# https://leetcode.com/problems/largest-rectangle-in-histogram/

# This problem can be efficiently solved using a monotonic stack.
# The stack stores indices of bars in increasing order of height.
# When a bar is popped, it means we found its right boundary, and the element below it in the stack is its left boundary.

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = [] # Stores indices of bars in increasing order of height

        # Iterate through all bars, including a sentinel bar of height 0 at the end
        # to ensure all bars in the stack are processed.
        for i, height in enumerate(heights + [0]):
            # While the stack is not empty and the current bar is shorter than