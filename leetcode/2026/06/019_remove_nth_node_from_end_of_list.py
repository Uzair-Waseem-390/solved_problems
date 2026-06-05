# Remove Nth Node From End of List
# Difficulty: Medium
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Using a dummy node and two pointers, fast_ptr and slow_ptr, to find the Nth node from the end in one pass.
# The fast_ptr maintains an n+1 node lead over slow_ptr.
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head

        slow_ptr = dummy_head
        fast_ptr = dummy_head

        for _ in range(n + 1):
            fast_ptr = fast_ptr.next

        while fast_ptr is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        slow_ptr.next = slow_ptr.next.next

        return dummy_head.next