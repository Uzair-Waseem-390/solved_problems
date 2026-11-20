# Reorder List
# Difficulty: Medium
# https://leetcode.com/problems/reorder-list/

# The strategy is to split the list into two halves, reverse the second half, and then interleave the nodes.
# Finding the middle: use slow and fast pointers. Slow moves one step, fast moves two.
# To handle both even and odd length lists, the first half should be slightly longer or equal for odd lengths.
# The `slow` pointer will end up at the end of the first half.
# Reverse the second half of the list.
# Merge the two lists by interleaving their nodes.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorder