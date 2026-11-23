# Binary Tree Preorder Traversal
# Difficulty: Easy
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Iterative preorder traversal uses a stack.
# Push the root, then repeatedly pop a node, add its value,
# and push its right child then its left child (LIFO order ensures left is processed before right).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        preorder_values = []
        if not root:
            return preorder_values

        node_stack = []
        node_stack.append(root)

        while node_stack:
            current_node = node_stack.pop()
            preorder_values.append(current_node.val)

            # For preorder (Root, Left, Right),
            # push Right child first, then Left child.
            # This ensures Left child is popped and processed before Right child
            # due to the LIFO nature of the stack.
            if current_node.right:
                node_stack.append(current_node.right)
            if current_node.left:
                node_stack.append(current_node.left)
        
        return preorder_values