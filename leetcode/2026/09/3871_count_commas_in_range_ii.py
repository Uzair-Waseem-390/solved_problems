# Count Commas in Range II
# Difficulty: Medium
# https://leetcode.com/problems/count-commas-in-range-ii/

# The problem asks to count commas in numbers up to N.
# We can iterate through groups of numbers that have the same number of commas (e.g., 1-999 have 0 commas, 1000-999999 have 1 comma, etc.).
# For each group, calculate how many numbers within that group fall into the [1, N] range and multiply by the number of commas for that group.
# Python's arbitrary-precision integers handle the large numbers (up to 10^15).

class Solution:
    def countCommas(self, n: int) -> int:
        total_commas_used = 0
        
        # 'num_commas