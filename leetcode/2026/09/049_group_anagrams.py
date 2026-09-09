# Group Anagrams
# Difficulty: Medium
# https://leetcode.com/problems/group-anagrams/

# Use a hash map where keys are character counts (as tuples) and values are lists of anagrams.
# This allows grouping strings by their canonical character frequency representation.
import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = collections.defaultdict(list)
        
        for current_string in strs:
            char_counts = [0] * 26
            for char_val in current_string:
                char_counts[ord(char_val) - ord('a')] += 1
            
            char_key = tuple(char_counts)
            anagram_map[char_key].append(current_string)
            
        return list(anagram_map.values())