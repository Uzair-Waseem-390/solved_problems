# Smallest Missing Multiple of K
# Difficulty: Easy
# https://leetcode.com/problems/smallest-missing-multiple-of-k/

# Convert nums to a set for O(1) lookups. Then iterate through multiples of k, starting from k, until a missing multiple is found.

class Solution:
    def smallestMissingMultiple(self, nums: list[int], k: int) -> int:
        nums_present = set(nums)
        
        current_multiple = k
        while True:
            if current_multiple not in nums_present:
                return current_multiple
            current_multiple += k