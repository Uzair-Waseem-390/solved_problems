# Unique Binary Search Trees
# Difficulty: Medium
# https://leetcode.com/problems/unique-binary-search-trees/

# Dynamic programming approach. The problem asks for the nth Catalan number, which can be computed using the recurrence relation:
# G(n) = sum(G(i-1) * G(n-i) for i from 1 to n), where G(0) = 1 and G(1) = 1.

class Solution:
    def numTrees(self, n: int) -> int:
        dp_table = [0] * (n + 1)
        dp_table[0] = 1

        for current_nodes in range(1, n + 1):
            for root_value in range(1, current_nodes + 1):
                left_subtree_nodes = root_value - 1
                right_subtree_nodes = current_nodes - root_value
                dp_table[current_nodes] += dp_table[left_subtree_nodes] * dp_table[right_subtree_nodes]
        
        return dp_table[n]