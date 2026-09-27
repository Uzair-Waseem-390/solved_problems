# Reverse Substrings Between Each Pair of Parentheses
# Difficulty: Medium
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

# Uses a stack to keep track of the starting index for each segment that needs to be reversed.
# When a closing parenthesis is encountered, the segment from the popped index to the current end of the result list is reversed in place.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        result_characters = []
        open_paren_indices = []

        for char in s:
            if char == '(':
                open_paren_indices.append(len(result_characters))
            elif char == ')':
                start_index_for_reverse = open_paren_indices.pop()
                result_characters[start_index_for_reverse:] = result_characters[start_index_for_reverse:][::-1]
            else:
                result_characters.append(char)
        
        return "".join(result_characters)