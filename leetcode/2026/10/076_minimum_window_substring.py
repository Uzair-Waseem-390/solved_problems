# Minimum Window Substring
# Difficulty: Hard
# https://leetcode.com/problems/minimum-window-substring/

# Sliding window approach: expand right pointer, then shrink left pointer when a valid window is found.
# Use two hash maps to track character counts for 't' and the current window.
# A counter 'chars_formed' tracks how many characters from 't' (including duplicates) are currently satisfied in the window.

import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        target_char_counts = collections.Counter(t)
        window_char_counts = collections.defaultdict(int)

        left = 0
        chars_formed = 0
        
        min_window_length = float('inf')
        min