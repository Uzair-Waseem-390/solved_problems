# Stone Game III
# Difficulty: Hard
# https://leetcode.com/problems/stone-game-iii/

# Dynamic programming approach. dp[i] stores the maximum net score (Alice's score - Bob's score)
# the current player can achieve starting from index i. We iterate backwards, calculating
# the optimal move by considering taking 1, 2, or 3 stones and subtracting the opponent's
# optimal net score from the remaining piles.

class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        num_stones = len(stoneValue)
        
        # dp[i] represents the maximum score difference (current player's score - opponent's score)
        # if the game starts from stoneValue[i].
        # We need N+3 elements to simplify boundary