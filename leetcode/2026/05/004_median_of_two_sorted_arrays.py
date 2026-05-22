# Median of Two Sorted Arrays
# Difficulty: Hard
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Binary search on the partition of the shorter array to find the correct split point
# that satisfies the median conditions in O(log(min(m, n))) time.
# Handle edge cases for empty partitions with negative/positive infinity.
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        low = 0
        high = m
        
        half_length = (m + n + 1) // 2

        while