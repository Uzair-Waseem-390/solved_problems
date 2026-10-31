# Path Sum
# Difficulty: Easy
# https://leetcode.com/problems/path-sum/

# DFS traversal, decrementing targetSum at each node.
# A path exists if we reach a leaf node and the remaining sum is 0.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        new_target_sum = targetSum - root.val
        
        return self.hasPathSum(root.left, new_target_sum) or \
               self.hasPathSum(root.right, new_target_sum)