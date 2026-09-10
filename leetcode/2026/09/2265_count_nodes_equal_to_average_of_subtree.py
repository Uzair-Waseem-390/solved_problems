# Count Nodes Equal to Average of Subtree
# Difficulty: Medium
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# A post-order DFS traversal is suitable here to compute subtree sums and counts from the bottom up.
# We'll return (subtree_sum, subtree_node_count) from the DFS and update a global counter.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.nodes_equal_to_average = 0

        def dfs(node):
            if not node:
                return (0, 0)

            left_subtree_sum, left_subtree_count = dfs(node.left)
            right_subtree_sum, right_subtree_count = dfs(node.right)

            current_subtree_sum = node.val + left_subtree_sum + right_subtree_sum
            current_subtree_count = 1 + left_subtree_count + right_subtree_count

            average_value = current_subtree_sum // current_subtree_count

            if node.val == average_value:
                self.nodes_equal_to_average += 1

            return (current_subtree_sum, current_subtree_count)

        dfs(root)
        return self.nodes_equal_to_average