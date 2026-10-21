# Validate Binary Search Tree
# Difficulty: Medium
# https://leetcode.com/problems/validate-binary-search-tree/

# Recursively validate BST properties by passing min/max bounds down the tree. Each node's value must be strictly within its inherited bounds.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check_node(node, min_bound, max_bound):
            if not node:
                return True

            if not (min_bound < node.val < max_bound):
                return False

            left_is_valid = check_node(node.left, min_bound, node.val)
            if not left_is_valid:
                return False

            right_is_valid = check_node(node.right, node.val, max_bound)
            if not right_is_valid:
                return False

            return True

        return check_node(root, float('-inf'), float('inf'))