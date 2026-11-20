# Maximize Consecutive Elements in an Array After Modification
# Difficulty: Hard
# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

import collections

class Solution:
    def maximizeConsecutive(self, nums: list[int]) -> int:
        # Sort the array to process elements in increasing order.
        # Use dynamic programming with a hash map (defaultdict) to store
        # the maximum length of a consecutive sequence ending at a specific value.
        # For each number `n` in the sorted array, it can either be used as `n`
        # or `n+1`. We update the DP states for both possibilities.
        # To handle duplicates correctly, we need to ensure that when `n` is processed,
        # the `dp[n-1]` and `dp[n]` values used for calculation reflect sequences
        # that *don't* include the