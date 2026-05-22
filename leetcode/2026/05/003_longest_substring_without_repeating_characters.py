# Longest Substring Without Repeating Characters
# Difficulty: Medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Use a sliding window approach with a hash set to keep track of characters in the current window.
# Expand the window with the right pointer, and shrink with the left pointer if a duplicate is found.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        max_length = 0
        current_window_characters = set()

        for right_pointer in range(len(s)):
            while s[right_pointer] in current_window_characters:
                current_window_characters.remove(s[left_pointer])
                left_pointer += 1
            
            current_window_characters.add(s[right_pointer])
            max_length = max(max_length, right_pointer - left_pointer + 1)
        
        return max_length