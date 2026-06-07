# Create Binary Tree From Descriptions
# Difficulty: Medium
# https://leetcode.com/problems/create-binary-tree-from-descriptions/

# Build nodes and track children using a map and a set. Connect nodes based on descriptions. The root is the node that is never a child.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        node_map = {}
        child_nodes = set()

        for parent_val, child_val, is_left in descriptions:
            if parent_val not in node_map:
                node_map[parent_val] = TreeNode(parent_val)
            if child_val not in node_map:
                node_map[child_val] = TreeNode(child_val)
            
            child_nodes.add(child_val)

            parent_node = node_map[parent_val]
            child_node = node_map[child_val]

            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        
        root_val = -1
        for node_val in node_map:
            if node_val not in child_nodes:
                root_val = node_val
                break
        
        return node_map[root_val]