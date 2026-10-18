# Unique Binary Search Trees II
# Difficulty: Medium
# https://leetcode.com/problems/unique-binary-search-trees-ii/

# This problem can be solved recursively by considering each number from `start` to `end` as the root,
# then recursively generating all possible left subtrees from `start` to `root-1` and right subtrees from `root+1` to `end`.
# The base cases handle empty subtrees (returning `[None]`) and single-node subtrees.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_trees_recursive(start_val: int, end_val: int) -> List[Optional[TreeNode]]:
            if start_val > end_val:
                return [None]
            
            if start_val == end_val:
                return [TreeNode(start_val)]

            all_possible_trees = []
            for root_val in range(start_val, end_val + 1):
                left_trees = generate_trees_recursive(start_val, root_val - 1)
                right_trees = generate_trees_recursive(root_val + 1, end_val)

                for left_subtree in left_trees:
                    for right_subtree in right_trees:
                        current_root = TreeNode(root_val)
                        current_root.left = left_subtree
                        current_root.right = right_subtree
                        all_possible_trees.append(current_root)
            
            return all_possible_trees

        return generate_trees_recursive(1, n) if n >= 1 else []