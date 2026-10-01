# Climbing Stairs
# Difficulty: Easy
# https://leetcode.com/problems/climbing-stairs/

# This problem can be solved using dynamic programming, recognizing that the number of ways to reach step `n` is the sum of ways to reach `n-1` (by taking 1 step) and ways to reach `n-2` (by taking 2 steps). This forms the Fibonacci sequence, which can be computed iteratively.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # Base cases for Fibonacci sequence
        # ways_to_two_steps_back represents F(i-2)
        # ways_to_one_step_back represents F(i-1)
        ways_to_two_steps_back = 1  # Ways to reach step 1 (F(1))
        ways_to_one_step_back = 2   # Ways to reach step 2 (F(2))
        
        # Iterate from step 3 up to n
        for _ in range(3, n + 1):
            current_ways = ways_to_one_step_back + ways_to_two_steps_back
            ways_to_two_steps_back = ways_to_one_step_back
            ways_to_one_step_back = current_ways
            
        return ways_to_one_step_back