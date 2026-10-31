# Flatten Binary Tree to Linked List
# Difficulty: Medium
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# In-place flattening using an iterative approach. For each node, if it has a left child,
# we find the rightmost node of the left subtree and attach the current node's original right subtree
# to it. Then, we move the left subtree to the current node's right, and set left to null.
# Finally, we move to the next node in the flattened list. This simulates pre-order traversal.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root: