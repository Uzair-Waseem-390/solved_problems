# Add Two Numbers
# Difficulty: Medium
# https://leetcode.com/problems/add-two-numbers/

# Iterate through both linked lists, summing digits and handling carry-over just like manual addition. A dummy head simplifies result list construction.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current_node = dummy_head
        carry = 0

        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            sum_digits = digit1 + digit2 + carry
            new_digit = sum_digits % 10
            carry = sum_digits // 10

            current_node.next = ListNode(new_digit)
            current_node = current_node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next