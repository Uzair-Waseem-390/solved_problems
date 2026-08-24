# Longest Valid Parentheses
# Difficulty: Hard
# https://leetcode.com/problems/longest-valid-parentheses/

# Using a stack to keep track of indices of opening parentheses and unmatched closing parentheses.
# The stack stores -1 initially to handle cases starting with ')' or for length calculations.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        index_stack = [-1] 

        for i in range(len(s)):
            if s[i] == '(':
                index_stack.append(i)
            else:  # s[i] == ')'
                index_stack.pop()
                if not index_stack:
                    index_stack.append(i)
                else:
                    max_length = max(max_length, i -