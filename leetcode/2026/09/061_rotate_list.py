# Rotate List
# Difficulty: Medium
# https://leetcode.com/problems/rotate-list/

# Calculate list length and connect tail to head to form a circle. Then break the circle at the new tail to get the rotated list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        current_node = head
        length = 1
        while current_node.next:
            current_node = current_node.next
            length += 1
        
        original_tail = current_node

        effective_k = k % length
        if effective_k == 0:
            return head

        nodes_to_traverse_for_new_tail = length - effective_k - 1
        
        new_tail = head
        for _ in range(nodes_to_traverse_for_new_tail):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        original_tail.next = head
        new_tail.next = None
        
        return new_head