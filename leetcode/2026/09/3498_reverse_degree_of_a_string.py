# Reverse Degree of a String
# Difficulty: Easy
# https://leetcode.com/problems/reverse-degree-of-a-string/

# Iterate through the string, calculate reversed alphabet position and 1-indexed string position for each character,
# multiply them, and sum up all products.

class Solution:
    def reverseDegree(self, s: str) -> int:
        total_reverse_degree = 0
        
        for char_index in range(len(s)):
            current_char = s[char_index]
            
            alphabet_offset = ord(current_char) - ord('a')
            
            reversed_alphabet_position = 26 - alphabet_offset
            
            string_position = char_index + 1
            
            total_reverse_degree += reversed_alphabet_position * string_position
            
        return total_reverse_degree