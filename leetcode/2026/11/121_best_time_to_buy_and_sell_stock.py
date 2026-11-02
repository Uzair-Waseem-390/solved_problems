# Best Time to Buy and Sell Stock
# Difficulty: Easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# This problem can be solved in a single pass by keeping track of the minimum price encountered so far
# and updating the maximum profit whenever a higher price is found relative to that minimum.

import math

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum_buy_price = math.inf
        maximum_profit = 0

        for current_price in prices:
            if current_price < minimum_buy_price:
                minimum_buy_price = current_price
            else:
                current_profit = current_price - minimum_buy_price
                if current_profit > maximum_profit:
                    maximum_profit = current_profit
        
        return maximum_profit