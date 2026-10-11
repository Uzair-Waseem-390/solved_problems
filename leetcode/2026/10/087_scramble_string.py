# Scramble String
# Difficulty: Hard
# https://leetcode.com/problems/scramble-string/

# Memoized recursion with character count pruning for efficiency
# The core idea is to try all possible split points and two arrangements (swapped/not swapped)
# for the two substrings, using a dictionary to store results of subproblems.

from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def solve(sub1: str, sub2: str) -> bool:
            if (sub1, sub2) in memo:
                return memo[(sub1, sub2)]

            if sub1 == sub2:
                memo[(sub1, sub2)] = True
                return True

            n = len(sub1)