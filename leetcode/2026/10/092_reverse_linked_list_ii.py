# Reverse Linked List II
# Difficulty: Medium
# https://leetcode.com/problems/reverse-linked-list-ii/

# Traverse to the node before 'left', then reverse the sublist from 'left' to 'right' in place,
# finally connect the three parts: head, reversed sublist, and tail. Use a dummy node for edge cases.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        node_before_left = dummy
        for _ in range(left - 1):
            node_before_left = node_before_left.next
        
        left_node = node_before_left.next
        reversed_sublist_curr = node_before_left.next

        reversed_sublist_prev = None

        for _ in range(right - left + 1):
            next_node_to_reverse = reversed_sublist_curr.next
            reversed_sublist_curr.next = reversed_sublist_prev
            reversed_sublist_prev = reversed_sublist_curr
            reversed_sublist_curr = next_node_to_reverse
        
        node_before_left.next = reversed_sublist_prev
        left_node.next = reversed_sublist_curr

        return dummy.next