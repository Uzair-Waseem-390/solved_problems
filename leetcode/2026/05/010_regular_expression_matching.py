# Regular Expression Matching
# Difficulty: Hard
# https://leetcode.com/problems/regular-expression-matching/

# This problem can be solved using recursion with memoization (top-down dynamic programming).
# The key is to handle the '*' character, which can match zero or more occurrences of the preceding element,
# leading to two main recursive branches.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_char_matches = (i < len(s)) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j+1] == '*':
                # Option 1: '*' matches zero occurrences of the preceding element.
                # Advance pattern by 2 (skip p[j] and p[j+1]).
                # OR
                # Option 2: '*' matches one or more occurrences of the preceding element.
                # This is only possible if first_char_matches is true.
                # If so, consume s[i] and try to match the rest of s (s[i+1:])
                # with the same pattern (p[j:]) because '*' can match multiple times.
                result = dp(i, j + 2) or \
                         (first_char_matches and dp(i + 1, j))
            else:
                # No '*' after p[j]. The current characters must match,
                # then proceed to match the rest of the strings.
                result = first_char_matches and dp(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dp(0, 0)