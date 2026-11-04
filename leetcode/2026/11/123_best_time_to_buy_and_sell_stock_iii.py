# Best Time to Buy and Sell Stock III
# Difficulty: Hard
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# This problem can be solved using dynamic programming. We need to track the maximum profit for up to two transactions.
# For each day, we maintain four states:
# 1. `buy1_profit`: max profit after the first buy (negative, as it's money spent)
# 2. `sell1_profit`: max profit after the first sell
# 3. `buy2_profit`: max profit after the second buy (money spent after first transaction)
# 4. `sell2_profit`: max profit after the second sell (final profit)
# The updates for these states must be done in reverse order or using temporary variables to ensure
# that calculations for a state depend only on the previous day's states, not the current day'