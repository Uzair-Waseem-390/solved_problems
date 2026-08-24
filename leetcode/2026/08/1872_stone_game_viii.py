# Stone Game VIII
# Difficulty: Hard
# https://leetcode.com/problems/stone-game-viii/

# This is a game theory problem solvable with dynamic programming and prefix sums.
# The key insight is that the game state can be represented by `dp[i]`, which is the maximum score
# difference achievable if the first `i` original stones have been combined into a single stone,
# and the remaining stones are `stones[i], ..., stones[n-1]`.
# `dp[i]` is computed from right to left, using a suffix maximum optimization.

class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        num_stones = len(stones)

        prefix_sums = [0] * (num_stones + 1)
        for i in range(num_stones):
            prefix