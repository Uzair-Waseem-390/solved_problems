# Maximum K to Sort a Permutation
# Difficulty: Medium
# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

# The maximum k must be a submask of the bitwise AND of all elements that are not in their correct positions.
# This value of k also guarantees that all misplaced elements can be connected via swaps.

class Solution:
    def maximumK(self, nums: list[int]) -> int:
        n = len(nums)
        
        misplaced_elements_and = -1 # All bits set initially, equivalent to (1 << max_bits) - 1
        
        is_sorted = True
        for i in range(n):
            if nums[i] != i:
                is_sorted = False
                if misplaced_elements_and == -1: # First misplaced element
                    misplaced_elements_