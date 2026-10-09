# Remove Duplicates from Sorted List
# Difficulty: Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Iterate through the linked list, comparing each node's value with its successor.
# If duplicates are found, update the current node's next pointer to skip the duplicate.
# Otherwise, advance to the next node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        currentNode = head
        while currentNode and currentNode.next:
            if currentNode.val == currentNode.next.val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        
        return head