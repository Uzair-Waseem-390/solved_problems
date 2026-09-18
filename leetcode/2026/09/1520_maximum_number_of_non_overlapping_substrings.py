# Maximum Number of Non-Overlapping Substrings
# Difficulty: Hard
# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

# Precompute first and last occurrences of each character.
# Then iterate through possible start indices. If an index is the first occurrence of its character,
# expand its range to the right to include all occurrences of characters within the range.
# If at any point a character within the range has its first occurrence before the current start index,
# this start index is invalid.
# Collect all valid minimal substrings, then greedily select non-overlapping ones by picking
# those with the smallest end index (and implicitly, smallest length for the same start).

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        string_length = len(s)
        first_occurrence = {}
        last_occurrence