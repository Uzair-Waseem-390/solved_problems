# Jump Game V
# Difficulty: Hard
# https://leetcode.com/problems/jump-game-v/

# This problem asks for the longest path in a directed acyclic graph (DAG) where nodes are array indices
# and edges are valid jumps. Since jumps are always from higher to lower values, it's a DAG.
# Memoized recursion (top-down dynamic programming) is a natural fit. dp[i] stores the max jumps from index i.

import sys

class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        memo = [0] * n
        
        # Increase recursion limit for potentially deep paths
        sys.setrecursionlimit(n + 100) 

        def find_max_jumps_from_