# Minimum Depth of Binary Tree
# Difficulty: Easy
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Using BFS to find the shortest path to any leaf node.
# BFS naturally explores level by level, guaranteeing the first leaf found is at the minimum depth.
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        node_queue = collections.deque([(root, 1)])

        while node_queue:
            current_node, current_depth = node_queue.popleft()

            if not current_node.left and not current_node.right:
                return current_depth

            if current_node.left:
                node_queue.append((current_node.left, current_depth + 1))
            if current_node.right:
                node_queue.append((current_node.right, current_depth + 1))