# Convert Sorted Array to Binary Search Tree
# Difficulty: Easy
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# This problem can be solved recursively by picking the middle element of the sorted array as the root of the BST.
# The left half of the array forms the left subtree, and the right half forms the right subtree, ensuring height balance.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        
        def build_bst_recursive(left_index: int, right_index: int) -> TreeNode:
            if left_index > right_index:
                return None

            middle_index = (left_index + right_index) // 2
            root_node = TreeNode(nums[middle_index])

            root_node.left = build_bst_recursive(left_index, middle_index - 1)
            root_node.right = build_bst_recursive(middle_index + 1, right_index)

            return root_node

        return build_bst_recursive(0, len(nums) - 1)