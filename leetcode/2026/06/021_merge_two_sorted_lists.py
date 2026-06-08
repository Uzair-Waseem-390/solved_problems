# Merge Two Sorted Lists
# Difficulty: Easy
# https://leetcode.com/problems/merge-two-sorted-lists/

# Recursive approach works well here, breaking down the problem by picking the smaller head and merging the rest.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        merged_head = None
        if list1.val <= list2.val:
            merged_head = list1
            merged_head.next = self.mergeTwoLists(list1.next, list2)
        else:
            merged_head = list2
            merged_head.next = self.mergeTwoLists(list1, list2.next)
        
        return merged_head