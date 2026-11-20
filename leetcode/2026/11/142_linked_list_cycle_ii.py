# Linked List Cycle II
# Difficulty: Medium
# https://leetcode.com/problems/linked-list-cycle-ii/

# Uses Floyd's Cycle Finding Algorithm (tortoise and hare) to first detect a cycle, then determine the starting node of the cycle in O(1) space.
# The core idea is that if a cycle exists, slow and fast pointers will meet. Then, resetting one pointer to the head and moving both at the same speed will lead them to meet at the cycle's beginning.

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow_pointer = head
        fast_pointer = head

        # Phase 1: Detect if a cycle exists
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                break
        else:
            # No cycle found (fast_pointer reached end of list)
            return None

        # Phase 2: Find the start of the cycle
        # If a cycle exists, slow_pointer and fast_pointer have met.
        # Reset slow_pointer to the head.
        # Move both pointers one step at a time; they will meet at the cycle start.
        slow_pointer = head
        while slow_pointer != fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        
        return slow_pointer