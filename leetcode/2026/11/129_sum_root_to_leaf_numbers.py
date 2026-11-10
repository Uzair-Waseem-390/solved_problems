# Sum Root to Leaf Numbers
# Difficulty: Medium
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# DFS traversal to build numbers along root-to-leaf paths.
# At each step, multiply the current path number by 10 and add the node's value.
# When a leaf is reached, add the completed number to the total sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0

        def dfs(node, current_path_number):
            nonlocal total_sum

            if not node:
                return

            current_path_number = current_path_number * 10 + node.val

            if not node.left and not node.right:
                total_sum += current_path_number
                return

            dfs(node.left, current_path_number)
            dfs(node.right, current_path_number)

        dfs(root, 0)
        return total_sum