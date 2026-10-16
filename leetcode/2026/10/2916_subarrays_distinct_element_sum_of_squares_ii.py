# Subarrays Distinct Element Sum of Squares II
# Difficulty: Hard
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

# This problem can be efficiently solved using a segment tree with lazy propagation.
# For each element nums[j], we update the distinct counts of subarrays ending at j.
# If nums[j] was last seen at prev_idx, then distinct counts for subarrays starting at [prev_idx+1, j] increase by 1.
# The segment tree stores (sum of distinct counts, sum of squares of distinct counts) for ranges,
# allowing O(logN) range updates and queries.

class Solution:
    def sumOfSquaresOfDistinctCounts(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        # Segment tree nodes store (sum_distincts