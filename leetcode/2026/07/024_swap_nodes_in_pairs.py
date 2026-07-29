# Swap Nodes in Pairs
# Difficulty: Medium
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Recursive approach is clean for this problem. The base cases are an empty list or a single-node list.
# For a pair, swap the current two nodes and then recursively call for the rest of the list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node