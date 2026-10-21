# Minimum Operations to Sort a String
# Difficulty: Medium
# https://leetcode.com/problems/minimum-operations-to-sort-a-string/

class Solution:
    def minimumOperations(self, s: str) -> int:
        # Categorize cases: 0 for already sorted, -1 for impossible (length 2, out of order),
        # 1 if min char is at start or max char is at end (allowing 1 op to sort rest),
        # 2 if min char can be moved to start via one prefix sort, or max char to end via one suffix sort,
        # 3 if neither of the above apply but string can be sorted.

        string_length = len(s)
        sorted_s_chars = sorted(list(s))
        min_char = sorted_s_chars[0]
        max_char =