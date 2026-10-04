# Valid Parenthesis String
# Difficulty: Medium
# https://leetcode.com/problems/valid-parenthesis-string/

# This problem can be solved with a greedy approach using two counters.
# One counter tracks the minimum possible open parentheses count,
# and the other tracks the maximum possible open parentheses count.
# We iterate through the string, updating these counts based on '(', ')', or '*'.
# The string is valid if the maximum count never drops below zero during iteration,
# and the minimum count is zero at the end.

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open_count = 0
        max_open_count = 0

        for char in s:
            if char == '(':
                min_open_count += 1
                max_open_count += 1