# Total Waviness of Numbers in Range II
# Difficulty: Hard
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

# This is a digit DP problem. The state needs to track the current index, tight constraint,
# and the two previous digits to determine peaks/valleys. Memoization stores (count, total_waviness).

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        memo = {}
        s_num_str = "" # Will be set for each call to `calculate`

        def dp(idx: int, tight: bool, prev_prev_digit: int, prev_digit: int, is_leading_zero: bool) -> tuple[int, int]:
            # prev_prev_digit and prev_digit are -1 if they haven't been set yet