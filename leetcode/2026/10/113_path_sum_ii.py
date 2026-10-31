# Path Sum II
# Difficulty: Medium
# https://leetcode.com/problems/path-sum-ii/

# Use a depth-first search (DFS) with backtracking to explore all root-to-leaf paths.
# Keep track of the current path and the remaining sum needed, adding paths when a leaf is reached and sum matches.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        all_paths = []

        def dfs(node: Optional[TreeNode], current_path: List[int], remaining_target: int):
            if not node:
                return

            current_path.append(node.val)

            if not node.left and not node.right:
                if remaining_target - node.val == 0:
                    all_paths.append(list(current_path))
            else:
                dfs(node.left, current_path, remaining_target - node.val)
                dfs(node.right, current_path, remaining_target - node.val)

            current_path.pop()

        dfs(root, [], targetSum)
        return all_paths