# Zigzag Conversion
# Difficulty: Medium
# https://leetcode.com/problems/zigzag-conversion/

# Simulating the zigzag pattern by appending characters to a list of row strings.
# A direction variable tracks whether we are moving down or up the rows, flipping at the boundaries.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        row_characters = [[] for _ in range(numRows)]
        
        current_row = 0
        going_down = True

        for character in s:
            row_characters[current_row].append(character)

            if going_down:
                current_row += 1
                if current_row == numRows:
                    going_down = False