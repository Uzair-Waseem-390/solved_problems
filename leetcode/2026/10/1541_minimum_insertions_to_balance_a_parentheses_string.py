# Minimum Insertions to Balance a Parentheses String
# Difficulty: Medium
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

# This problem can be solved with a single pass, keeping track of open parentheses count.
# When encountering a closing parenthesis, we check if it's a single ')' or a ')).'
# We greedily match ')' or '))' with an open '(', or insert ')' or '(' as needed.

class Solution:
    def minInsertions(self, s: str) -> int:
        insertions_needed = 0
        open_parens_balance = 0
        
        i = 0
        while i < len(s):
            char = s[i]
            
            if char == '(':
                open_parens_balance += 1
            else: # char == ')'