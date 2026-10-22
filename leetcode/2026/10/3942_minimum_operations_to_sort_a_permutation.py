# Minimum Operations to Sort a Permutation
# Difficulty: Medium
# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

# BFS approach to find the minimum operations. States are (type, shift) based on whether the array is a rotation of the sorted sequence or its reverse.
# The target state is (0, 0), representing the sorted array [0, 1, ..., n-1].

import collections

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        n = len(nums)

        # Precompute positions of elements for O(1) lookup
        # pos[val] gives the index of `val` in `nums`
        pos = [0] * n
        for i in range(n):
            pos[nums[i]] = i

        # Determine the initial state (type, shift) for