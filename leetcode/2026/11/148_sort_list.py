# Sort List
# Difficulty: Medium
# https://leetcode.com/problems/sort-list/

# Recursive merge sort for linked lists.
# Split the list into two halves using fast/slow pointers,
# recursively sort each half, then merge the two sorted halves.
# This provides O(n log n) time complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow_pointer = head
        fast_pointer = head
        previous_to_slow = None

        while fast_