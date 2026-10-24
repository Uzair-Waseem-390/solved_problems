# Binary Tree Zigzag Level Order Traversal
# Difficulty: Medium
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Standard BFS level order traversal, but toggle a flag to reverse the list of values for odd-numbered levels.
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> list[list[int]]:
        if not root:
            return []

        all_level_values = []
        node_queue = collections.deque([root])
        is_left_to_right_direction = True

        while node_queue:
            level_nodes_count = len(node_queue)
            current_level_values = []

            for _ in range(level_nodes_count):
                node = node_queue.popleft()
                current_level_values.append(node.val)

                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            
            if not is_left_to_right_direction:
                current_level_values.reverse()
            
            all_level_values.append(current_level_values)
            is_left_to_right_direction = not is_left_to_right_direction
        
        return all_level_values