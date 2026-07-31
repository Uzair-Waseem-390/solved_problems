# Minimum Number of Pushes to Type Word II
# Difficulty: Medium
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

# Greedy approach: assign most frequent characters to slots with fewer pushes.
# There are 8 keys, so 8 slots for 1 push, then 8 for 2 pushes, etc.

import collections

class Solution:
    def minimumPushes(self, word: str) -> int:
        char_counts = collections.Counter(word)
        sorted_frequencies = sorted(char_counts.values(), reverse=True)
        
        total_pushes = 0
        current_push_multiplier = 1
        chars_assigned_to_current_level = 0
        
        for frequency in sorted_frequencies:
            total_pushes += frequency * current_push_multiplier
            chars_assigned_to_current_level += 1
            
            if chars_assigned_to_current_level == 8:
                current_push_multiplier += 1
                chars_assigned_to_current_level = 0
                
        return total_pushes