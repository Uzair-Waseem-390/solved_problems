# Reverse Nodes in k-Group
# Difficulty: Hard
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Iteratively reverse k nodes at a time, using a dummy node to simplify head management.
# The core idea is to identify the k-node segment, reverse it, and then connect it to the rest of the list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        dummy_head = ListNode(0)
        dummy_head.next = head
        
        previous_segment_tail = dummy_head
        
        while True:
            # Check