# Word Search
# Difficulty: Medium
# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def search_word(row, col, word_index):
            if word_index == len(word):
                return True
            
            if not (0 <= row < rows and 0 <= col < cols) or board[row][col] != word[word_index]:
                return False
            
            original_char = board[row][col]
            board[row][col] = '#' 
            
            found = (search_word(row + 1, col, word_index + 1) or
                     search_word(row - 1, col, word_index + 1) or
                     search_word(row, col + 1, word_index + 1) or
                     search_word(row, col - 1, word_index + 1))
            
            board[row][col] = original_char
            
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if search_word(r, c, 0):
                        return True
        
        return False