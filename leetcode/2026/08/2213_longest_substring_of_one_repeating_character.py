# Longest Substring of One Repeating Character
# Difficulty: Hard
# https://leetcode.com/problems/longest-substring-of-one-repeating-character/

# A segment tree is used to efficiently handle point updates and query the longest repeating character substring.
# Each node stores max_len, prefix_len, suffix_len, left_char, right_char, and total_len,
# allowing for O(log N) updates and O(1) query of the overall max_len after each update.

class Node:
    def __init__(self, max_len=0, prefix_len=0, suffix_len=0, left_char='', right_char='', total_len=0):
        self.max_len = max_len
        self.prefix_len = prefix_len
        self.suffix_len = suffix_len
        self.left_char = left_char