# Binary Tree Level Order Traversal II
# Difficulty: Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Standard BFS approach, storing levels as we go, then reversing the final list of levels to get bottom-up order.
# Using a deque for efficient queue operations.
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        levels = []
        node_queue = collections.deque([root])

        while node_queue:
            level_size = len(node_queue)
            current_level_values = []
            for _ in range(level_size):
                current_node = node_queue.popleft()
                current_level_values.append(current_node.val)

                if current_node.left:
                    node_queue.append(current_node.left)
                if current_node.right:
                    node_queue.append(current_node.right)
            levels.append(current_level_values)

        return levels[::-1]