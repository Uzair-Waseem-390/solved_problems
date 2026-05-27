# Count the Number of Special Characters II
# Difficulty: Medium
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/

# Store last seen index for each lowercase char and first seen index for each uppercase char.
# Then iterate 'a' through 'z' to check if both exist and satisfy the order condition.
class Solution:
    def countSpecialCharacters(self, word: str) -> int:
        last_lower_char_indices = [-1] * 26
        first_upper_char_indices = [-1] * 26

        for i, char_code in enumerate(word):
            if 'a' <= char_code <= 'z':
                last_lower_char_indices[ord(char_code) - ord('a')] = i
            elif 'A' <= char_code <= 'Z':
                if first_upper_char_indices[ord(char_code) - ord('A')] == -1:
                    first_upper_char_indices[ord(char_code) - ord('A')] = i
        
        special_char_count = 0
        for i in range(26):
            if last_lower_char_indices[i] != -1 and first_upper_char_indices[i] != -1:
                if last_lower_char_indices[i] < first_upper_char_indices[i]:
                    special_char_count += 1
        
        return special_char_count