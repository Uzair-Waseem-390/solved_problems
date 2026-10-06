# Minimum Add to Make Parentheses Valid
# Difficulty: Medium
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

# This problem can be solved with a greedy approach by tracking the balance of open parentheses.
# We count unmatched closing parentheses and then unmatched opening parentheses.
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        current_open_parentheses = 0
        required_insertions = 0

        for char in s:
            if char == '(':
                current_open_parentheses += 1
            else:  # char == ')'
                if current_open_parentheses > 0:
                    current_open_parentheses -= 1
                else:
                    required_insertions += 1
        
        required_insertions += current_open_parentheses
        
        return required_insertions