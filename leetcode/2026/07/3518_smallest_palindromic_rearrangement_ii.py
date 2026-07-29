# Smallest Palindromic Rearrangement II
# Difficulty: Hard
# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

import collections
import math

class Solution:
    def getPermutationsCount(self, remaining_length_to_fill: int, char_counts: collections.defaultdict, k_limit: int) -> int:
        if remaining_length_to_fill == 0:
            return 1

        # Calculate N! / (c1! * c2! * ...) where N is remaining_length_to_fill
        # and c_i are counts of characters.
        # Since k is small (<= 10^6), we only care about counts up to k_limit.
        # If the number of permutations exceeds k_limit, we can just return k_limit + 1.
        
        #