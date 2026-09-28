# Maximum Nesting Depth of the Parentheses
# Difficulty: Easy
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

# Iterate through the string, keeping track of the current nesting level and updating the maximum depth encountered.

class Solution:
    def maxDepth(self, s: str) -> int:
        current_nesting_depth = 0
        maximum_nesting_depth = 0

        for char in s:
            if char == '(':
                current_nesting_depth += 1
                maximum_nesting_depth = max(maximum_nesting_depth, current_nesting_depth)
            elif char == ')':
                current_nesting_depth -= 1
        
        return maximum_nesting_depth