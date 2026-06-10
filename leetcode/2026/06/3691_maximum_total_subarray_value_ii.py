# Maximum Total Subarray Value II
# Difficulty: Hard
# https://leetcode.com/problems/maximum-total-subarray-value-ii/

# The problem can be solved greedily by always picking the subarray with the maximum value.
# We use a max-heap to keep track of the largest available subarray values.
# For efficient range max/min queries, a sparse table (RMQ) is precomputed.

import heapq
import math

class Solution:
    def maximumTotalSubarrayValue(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Precompute log_2 values for sparse table queries
        # log_table[i] stores floor(log2(i))
        log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            log_table