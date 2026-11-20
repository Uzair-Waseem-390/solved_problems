# Linked List Cycle
# Difficulty: Easy
# https://leetcode.com/problems/linked-list-cycle/

# Use Floyd's Cycle Finding Algorithm (tortoise and hare) with two pointers.
# A fast pointer moves twice as fast as a slow pointer. If they meet, there's a cycle.
# If the fast pointer reaches the end of the list, there's no cycle.

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow_pointer = head
        fast_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        
        return False