# Minimum Operations to Make Elements Within K Subarrays Equal
# Difficulty: Hard
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

# The problem asks for k non-overlapping subarrays of size x, where each subarray has all equal elements.
# The optimal way to make elements in a window equal is to choose their median as the target value.
# We first precompute the minimum operations for every possible window of size x using a sliding window median approach with two heaps.
# Then, we use dynamic programming: dp[j][i] stores the minimum cost to obtain j subarrays, with the j-th subarray starting at index i.
# The DP transition involves finding the minimum of dp[j-1][p] for p <= i-x, which can be optimized using a prefix minimum.

import heapq

class Solution:
    def minOperationsToMakeElementsWithinKSubarraysEqual(self, nums