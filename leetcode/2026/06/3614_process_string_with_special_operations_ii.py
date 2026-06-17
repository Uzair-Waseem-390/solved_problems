# Process String with Special Operations II
# Difficulty: Hard
# https://leetcode.com/problems/process-string-with-special-operations-ii/

# This problem requires a reverse simulation approach due to potentially huge string lengths (up to 10^15).
# First, simulate forward to track string lengths after each operation, capping lengths at a practical maximum (2*10^15) to prevent overflow.
# Then, simulate backward. For each operation, determine how the target index `k` would have mapped to the string state before that operation.

class Solution:
    def kthCharacter(self, s: str, k: int) -> str:
        max_possible_len = 2 * 10**15 # A sufficiently large cap, k_max is 10^15
        
        lengths_after_op = []
        current_len = 0