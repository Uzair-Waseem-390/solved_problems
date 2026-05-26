# Count the Number of Special Characters I
# Difficulty: Easy
# https://leetcode.com/problems/count-the-number-of-special-characters-i/

# Use two sets to store unique lowercase and uppercase letters encountered. Then iterate through 'a' to 'z' and check if both forms of each letter are present.
class Solution:
    def countSpecialCharacters(self, word: str) -> int:
        lowercase_letters_present = set()
        uppercase_letters_present = set()

        for char in word:
            if 'a' <= char <= 'z':
                lowercase_letters_present.add(char)
            elif 'A' <= char <= 'Z':
                uppercase_letters_present.add(char)
        
        special_letters_count = 0
        for i in range(26):
            lower_char = chr(ord('a') + i)
            upper_char = chr(ord('A') + i)
            
            if lower_char in lowercase_letters_present and upper_char in uppercase_letters_present:
                special_letters_count += 1
                
        return special_letters_count