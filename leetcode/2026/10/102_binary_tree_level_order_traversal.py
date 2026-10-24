# Binary Tree Level Order Traversal
# Difficulty: Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Breadth-First Search (BFS) with a queue is ideal here to process nodes level by level.
# For each level, we get its size first, then iterate that many times to extract all nodes and enqueue their children.
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level_order_traversal = []
        node_queue = collections.deque([root])

        while node_queue:
            level_size = len(node_queue)
            current_level_values = []
            for _ in range(level_size):
                node = node_queue.popleft()
                current_level_values.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            level_order_traversal.append(current_level_values)

        return level_order_traversal