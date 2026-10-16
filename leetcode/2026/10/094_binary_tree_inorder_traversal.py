# Binary Tree Inorder Traversal
# Difficulty: Easy
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Iterative inorder traversal using a stack to simulate recursion. Keep pushing left children until null, then pop, record value, and move to right child.

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        inorder_values = []
        node_stack = []
        current_node = root

        while current_node is not None or node_stack:
            while current_node is not None:
                node_stack.append(current_node)
                current_node = current_node.left
            
            current_node = node_stack.pop()
            inorder_values.append(current_node.val)
            current_node = current_node.right
            
        return inorder_values