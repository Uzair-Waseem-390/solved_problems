# Number of Ways to Assign Edge Weights I
# Difficulty: Medium
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

import collections

class Solution:
    def numberOfWays(self, edges: list[list[int]]) -> int:
        # The core idea is to find the maximum depth of any node in the tree rooted at node 1.
        # For a path of length L (L edges), there are 2^(L-1) ways to assign weights 1 or 2
        # such that the total path cost is odd. This is because we need an odd number of 1s,
        # and the number of 2s does not affect parity.
        # A Breadth-First Search (BFS) is used to determine the maximum depth.
        
        num_nodes = len(edges) + 1
        
        adj_list