# Binary Tree Postorder Traversal
# Difficulty: Easy
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Iterative postorder traversal can be done by first getting a "Root, Right, Left" traversal and then reversing the result.
# This "Root, Right, Left" order is achieved by a standard iterative preorder logic, but pushing the right child to the stack before the left child.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        postorder_values_reversed = []
        node