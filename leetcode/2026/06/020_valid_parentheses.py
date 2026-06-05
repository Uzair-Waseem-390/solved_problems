# Valid Parentheses
# Difficulty: Easy
# https://leetcode.com/problems/valid-parentheses/

# Use a stack to keep track of open brackets. When a closing bracket is encountered, check if it matches the top of the stack.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        open_brackets = {'(', '{', '['}

        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:  # char is a closing bracket
                if not stack:
                    return False
                
                last_open_bracket = stack.pop()
                if bracket_map[char] != last_open_bracket:
                    return False
        
        return not stack