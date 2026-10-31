# Populating Next Right Pointers in Each Node
# Difficulty: Medium
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Iteratively traverse level by level, using the 'next' pointers established in the previous level
# to connect nodes in the current level. This achieves constant extra space.

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        level_head = root
        while level_head and level_head.left:
            current_node = level_head
            while current_node:
                current_node.left.next = current_node.right
                
                if current_node.next:
                    current_node.right.next = current_node.next.left
                
                current_node = current_node.next
            
            level_head = level_head.left
        
        return root