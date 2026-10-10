# Minimum Sum of Squared Difference
# Difficulty: Medium
# https://leetcode.com/problems/minimum-sum-of-squared-difference/

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_k_operations = k1 + k2

        max_possible_diff = 0
        # diff_frequencies stores the count of each absolute difference value
        # The maximum possible difference is 10^5, so array size 10^5 + 1 is sufficient.
        diff_frequencies = [0] * (10**5 + 1) 

        for i in range(n):
            current_abs_diff = abs(nums1[i] - nums2[i