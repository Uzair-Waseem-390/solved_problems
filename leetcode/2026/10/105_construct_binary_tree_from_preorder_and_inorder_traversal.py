# Construct Binary Tree from Preorder and Inorder Traversal
# Difficulty: Medium
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# This problem is a classic divide and conquer on trees. The first element of preorder traversal is always the root.
# Once the root is identified, its position in the inorder traversal splits the array into left and right subtrees.
# We can then determine the corresponding segments in the preorder array based on the size of the left subtree.
# Using a hash map for inorder element lookups optimizes finding the root's position from O(N) to O(1).

# Definition for a binary tree node (provided by LeetCode environment, not part of the solution code itself)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        inorder_val_to_index = {val: idx for idx, val in enumerate(inorder)}

        def build_subtree(preorder_start_idx: int, preorder_end_idx: int,
                          inorder_start_idx: int, inorder_end_idx: int) -> TreeNode:
            if preorder_start_idx > preorder_end_idx or inorder_start_idx > inorder_end_idx:
                return None

            root_value = preorder[preorder_start_idx]
            root = TreeNode(root_value)

            root_in_inorder_idx = inorder_val_to_index[root_value]
            left_subtree_size = root_in_inorder_idx - inorder_start_idx

            root.left = build_subtree(preorder_start_idx + 1,
                                      preorder_start_idx + left_subtree_size,
                                      inorder_start_idx,
                                      root_in_inorder_idx - 1)

            root.right = build_subtree(preorder_start_idx + left_subtree_size + 1,
                                       preorder_end_idx,
                                       root_in_inorder_idx + 1,
                                       inorder_end_idx)

            return root

        return build_subtree(0, len(preorder) - 1, 0, len(inorder) - 1)