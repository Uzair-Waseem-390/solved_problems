# Maximum Depth of Binary Tree
# Difficulty: Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Recursive DFS naturally solves this problem. The depth of a node is 1 plus the maximum depth of its left or right children.
# The base case is an empty tree (None), which has a depth of 0.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_subtree_depth = self.maxDepth(root.left)
        right_subtree_depth = self.maxDepth(root.right)

        return 1 + max(left_subtree_depth, right_subtree_depth)