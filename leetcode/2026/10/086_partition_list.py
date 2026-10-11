# Partition List
# Difficulty: Medium
# https://leetcode.com/problems/partition-list/

# Iterate through the original list, building two separate new lists: one for nodes less than x, and one for nodes greater or equal to x. Then, concatenate these two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_head = ListNode(0)
        less_tail = less_head

        greater_head = ListNode(0)
        greater_tail = greater_head

        current_node = head
        while current_node:
            if current_node.val < x:
                less_tail.next = current_node
                less_tail = less_tail.next
            else:
                greater_tail.next = current_node
                greater_tail = greater_tail.next
            current_node = current_node.next
        
        less_tail.next = greater_head.next
        greater_tail.next = None

        return less_head.next