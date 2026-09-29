# Text Justification
# Difficulty: Hard
# https://leetcode.com/problems/text-justification/

# This problem requires careful simulation of text formatting rules.
# The core idea is to greedily pack words into lines, then apply different justification rules for normal lines, single-word lines, and the last line.
# Tracking word lengths and available space accurately for each line is key.

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result_lines = []
        word_pointer = 0
        total_words = len(words)

        while word_pointer < total_words:
            current_line_words = []
            current_words_length = 0 # Sum of lengths of words in current_line_words

            # Add the first word to the current