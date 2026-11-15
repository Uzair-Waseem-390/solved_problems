# Copy List with Random Pointer
# Difficulty: Medium
# https://leetcode.com/problems/copy-list-with-random-pointer/

# Use a hash map to store mappings from original nodes to their new copies, allowing us to link both next and random pointers correctly in two passes.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node']':
        if not head:
            return None

        original_to_copy_map = {}
        
        current_original_node = head
        while current_original_node:
            new_node = Node(current_original_node.val)
            original_to_copy_map[current_original_node] = new_node
            current_original_node = current_original_node.next

        current_original_node = head
        while current_original_node:
            corresponding_new_node = original_to_copy_map[current_original_node]
            
            corresponding_new_node.next = original_to_copy_map.get(current_original_node.next)
            corresponding_new_node.random = original_to_copy_map.get(current_original_node.random)
            
            current_original_node = current_original_node.next
        
        return original_to_copy_map[head]