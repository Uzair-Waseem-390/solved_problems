# Merge k Sorted Lists
# Difficulty: Hard
# https://leetcode.com/problems/merge-k-sorted-lists/

# Use a min-priority queue (heap) to keep track of the smallest current node from all k lists.
# Repeatedly extract the minimum, append it to the result, and add its next node to the heap.
# A counter is used as a tie-breaker for heap elements with identical values.
import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        min_heap = []
        
        merged_head = ListNode()
        current_tail = merged_head
        
        counter = 0 
        for list_node in lists:
            if list_node:
                heapq.heappush(min_heap, (list_node.val, counter, list_node))
                counter += 1
                
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            
            current_tail.next = node
            current_tail = current_tail.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1
        
        return merged_head.next