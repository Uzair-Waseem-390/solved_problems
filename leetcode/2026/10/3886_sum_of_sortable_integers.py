# Sum of Sortable Integers
# Difficulty: Hard
# https://leetcode.com/problems/sum-of-sortable-integers/

# The problem requires iterating through all divisors 'k' of 'n'.
# For each 'k', we partition 'nums' into blocks of size 'k' and compare them with corresponding blocks from the globally sorted array.
# Two conditions must be met for each block:
# 1. The elements within the current block must be the same as the elements in the corresponding sorted block (checked efficiently using Counter).
# 2. The current block must be a cyclic rotation of the corresponding sorted block (checked by seeing if the sorted block is a "substring" of the current block concatenated with itself).
# If both conditions hold for all blocks, 'k' is sortable.

import collections

class Solution:
    def sumOfSortableIntegers(