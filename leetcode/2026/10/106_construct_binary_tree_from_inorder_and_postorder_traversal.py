# Construct Binary Tree from Inorder and Postorder Traversal
# Difficulty: Medium
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Recursive approach. The last element of postorder is the root. Find its position in inorder to split subtrees.
# Process postorder array from right to left (root, then right subtree, then left subtree).

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        inorder_value_to_index = {value: index for index, value in enumerate(inorder)}
        current_postorder_index = len(postorder) - 1

        def build_subtree(inorder_left_bound: int, inorder_right_bound: int) -> TreeNode | None:
            nonlocal current_postorder_index

            if inorder_left_bound > inorder_right_bound:
                return None

            root_value = postorder[current_postorder_index]
            root_node = TreeNode(root_value)
            current