# Count Non-Decreasing Subarrays After K Operations
# Difficulty: Hard
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

# Sliding window with a monotonic deque to efficiently calculate the sum of effective maximums.
# The deque stores (value, count) pairs, representing segments of equal effective values.
# When expanding the window, we update effective values and costs. When shrinking, we adjust costs based on the leftmost element.

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        total_valid_subarrays = 0
        left = 0
        current_cost = 0
        
        # Deque stores (value, count) pairs, representing segments where the effective value
        # for P[x] is 'value' for 'count' elements