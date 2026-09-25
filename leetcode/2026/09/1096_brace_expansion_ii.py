# Brace Expansion II
# Difficulty: Hard
# https://leetcode.com/problems/brace-expansion-ii/

# Recursive descent parser to handle union (comma-separated terms) and concatenation (sequence of factors).
# Factors are either single letters or expressions in braces.
# The parsing functions return a set of strings and the updated index in the expression.

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.expression = expression
        self.length = len(expression)

        # parse_factor handles the smallest units: single letters or brace-enclosed expressions.
        def parse_factor(index):
            if self.expression[index] == '{':
                # If it's an opening brace, parse the full expression inside it.
                index += 1  # Move past '{'
                sub