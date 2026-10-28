# Balanced Binary Tree
# Difficulty: Easy
# https://leetcode.com/problems/balanced-binary-tree/

# This problem can be solved with a single depth-first search (DFS) traversal.
# We define a helper function that simultaneously calculates the height of a subtree and checks if it's balanced.
# If an imbalance is detected at any point, a special value (e.g., -1) is returned to signal an unbalanced tree, propagating up the call stack.

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height_and_balance_status(node):
            if not node:
                return 0

            left_subtree_status = get_height_and_balance_status(node.left)
            if left_subtree_status == -1:
                return -1

            right_subtree_status = get_height_and_balance_status(node.right)
            if right_subtree_status == -1:
                return -1

            if abs(left_subtree_status - right_subtree_status) > 1:
                return -1
            
            return max(left_subtree_status, right_subtree_status) + 1
        
        return get_height_and_balance_status(root) != -1