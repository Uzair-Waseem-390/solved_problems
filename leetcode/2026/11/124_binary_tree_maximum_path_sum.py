# Binary Tree Maximum Path Sum
# Difficulty: Hard
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# DFS approach: For each node, calculate the max path sum that can extend upwards,
# and update the global max with paths that 'turn' at this node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum_tracker = [float('-inf')]

        def dfs_gain(node):
            if not node:
                return 0

            left_branch_gain = max(0, dfs_gain(node.left))
            right_branch_gain = max(0, dfs_gain(node.right))

            path_through_current_node = node.val + left_branch_gain + right_branch_gain
            
            max_sum_tracker[0] = max(max_sum_tracker[0], path_through_current_node)

            return node.val + max(left_branch_gain, right_branch_gain)

        dfs_gain(root)
        return max_sum_tracker[0]