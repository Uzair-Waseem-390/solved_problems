# Symmetric Tree
# Difficulty: Easy
# https://leetcode.com/problems/symmetric-tree/

# Recursive helper function compares left and right subtrees for mirror symmetry by checking values and cross-comparing children.
# This approach is clean and directly models the definition of symmetry.
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def check_mirror(left_node, right_node):
            if not left_node and not right_node:
                return True
            if not left_node or not right_node:
                return False
            
            return (left_node.val == right_node.val and
                    check_mirror(left_node.left, right_node.right) and
                    check_mirror(left_node.right, right_node.left))

        return check_mirror(root.left, root.right)