# Best Time to Buy and Sell Stock II
# Difficulty: Medium
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# The problem allows multiple transactions, so we can maximize profit by summing up every positive price difference.
# This greedy approach works because we can effectively buy low and sell high on consecutive days, accumulating all upward movements.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
                
        return total_profit