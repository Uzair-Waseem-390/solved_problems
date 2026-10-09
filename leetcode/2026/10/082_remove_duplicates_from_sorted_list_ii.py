# Remove Duplicates from Sorted List II
# Difficulty: Medium
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Use a dummy node to simplify head manipulation. Iterate with two pointers,
# `previous` and `current`. If `current` is the start of a duplicate sequence,
# find the end of that sequence and bypass all duplicate nodes by linking
# `previous.next` directly to the node after the sequence.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        previous = dummy
        current = head

        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next
        
        return dummy.next