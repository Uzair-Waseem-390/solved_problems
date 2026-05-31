# Longest Common Prefix
# Difficulty: Easy
# https://leetcode.com/problems/longest-common-prefix/

# Vertical scanning: iterate through characters of the first string, checking if all other strings match at each position.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        first_string = strs[0]
        
        for char_index in range(len(first_string)):
            currentChar = first_string[char_index]
            for other_string_index in range(1, len(strs)):
                if char_index >= len(strs[other_string_index]) or \
                   strs[other_string_index][char_index] != currentChar:
                    return first_string[0:char_index]
        
        return first_string