# Insertion Sort List
# Difficulty: Medium
# https://leetcode.com/problems/insertion-sort-list/

# Standard insertion sort logic applied to a linked list. We build a sorted list by iteratively removing nodes from the unsorted portion and inserting them into the correct position in the sorted portion.
# A dummy node simplifies insertions at the head of the sorted list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0)
        currentUnsorted = head

        while currentUnsorted:
            nextUnsortedNode = currentUnsorted.next

            prevSorted = dummy
            currentSorted = dummy.next

            while currentSorted and currentUnsorted.val > currentSorted.val:
                prevSorted = currentSorted
                currentSorted = currentSorted.next
            
            currentUnsorted.next = prevSorted.next
            prevSorted.next = currentUnsorted
            
            currentUnsorted = nextUnsortedNode
        
        return dummy.next