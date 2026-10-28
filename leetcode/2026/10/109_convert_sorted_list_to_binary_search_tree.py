# Convert Sorted List to Binary Search Tree
# Difficulty: Medium
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# The most efficient approach here is to use a bottom-up construction.
# First, determine the length of the linked list. Then, recursively build the tree
# from the leaves up, using a "global" pointer to consume linked list nodes in sorted order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    current_list_node = None

    def sortedListToBST(self, head: ListNode) -> TreeNode