# Populating Next Right Pointers in Each Node II
# Difficulty: Medium
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Iterative BFS using existing 'next' pointers to achieve O(1) extra space.
# We build the next level's connections while iterating through the current level.
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        current_level_head = root

        while current_level_head:
            next_level_head = None
            prev_node_in_next_level = None

            iterator_node = current_level_head
            while iterator_node:
                if iterator_node.left:
                    if prev_node_in_next_level:
                        prev_node_in_next_level.next = iterator_node.left
                    else:
                        next_level_head = iterator_node.left
                    prev_node_in_next_level = iterator_node.left
                
                if iterator_node.right:
                    if prev_node_in_next_level:
                        prev_node_in_next_level.next = iterator_node.right
                    else:
                        next_level_head = iterator_node.right
                    prev_node_in_next_level = iterator_node.right
                
                iterator_node = iterator_node.next
            
            current_level_head = next_level_head
        
        return root