# Shortest and Lexicographically Smallest Beautiful String
# Difficulty: Medium
# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

# Sliding window approach to find substrings with exactly k ones.
# We iterate with a right pointer, expanding the window. When k ones are found,
# we try to shrink from the left to find the shortest possible substring with k ones.
# We keep track of the shortest length and the lexicographically smallest string found so far.
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left_pointer = 0
        current_ones_count = 0
        min_length = float('inf')
        result_beautiful_string = ""

        for right_pointer in range(len(s)):
            if s[right_pointer] == '1':
                current_ones