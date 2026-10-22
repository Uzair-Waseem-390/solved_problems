# Recover Binary Search Tree
# Difficulty: Medium
# https://leetcode.com/problems/recover-binary-search-tree/

# In-order traversal of a BST yields a sorted sequence.
# Two swapped nodes will cause exactly one or two violations of this sorted order.
# The first violation's 'prev' node is the first swapped node. The second violation's 'current' node is the second.
# If only one violation, the 'current' node of that violation is the second swapped node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything