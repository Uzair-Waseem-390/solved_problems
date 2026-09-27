# Permutation Sequence
# Difficulty: Hard
# https://leetcode.com/problems/permutation-sequence/

# This problem can be solved by a mathematical approach, iteratively determining each digit
# from left to right. We use factorials to determine which block of permutations 'k' falls into
# for the current set of available numbers, effectively finding the correct digit at each position.

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutation_chars = []
        
        available_digits = [str(i) for i in range(1, n + 1)]
        
        factorials = [1] * (n + 1)
        for i in range(1, n + 1):
            factorials[i] = factorials[i-1] * i
        
        k -= 1 
        
        for current_n in range(n, 0, -1):
            block_size = factorials[current_n - 1]
            
            digit_index = k // block_size
            
            permutation_chars.append(available_digits[digit_index])
            
            available_digits.pop(digit_index)
            
            k %= block_size
            
        return "".join(permutation_chars)