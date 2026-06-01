# Minimum Cost of Buying Candies With Discount
# Difficulty: Easy
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

# To minimize the total cost, we should maximize the value of candies we get for free.
# Sorting the candies in descending order allows us to pick the two most expensive available candies to buy,
# and then the third most expensive available candy will always be eligible for free.
# We iterate, buying two candies and skipping the third.

class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        total_buying_cost = 0
        num_candies = len(cost)
        
        for i in range(0, num_candies, 3):
            total_buying_cost += cost[i]
            
            if i + 1 < num_candies:
                total_buying_cost += cost[i + 1]
            
            # The candy at cost[i+2] is implicitly skipped (taken for free)
            # because the loop increments 'i' by 3, effectively skipping it.
            # No explicit check is needed for free candy eligibility since
            # sorting ensures cost[i+2] <= cost[i+1] <= cost[i].
            # Thus, cost[i+2] is always less than or equal to min(cost[i], cost[i+1]).
            
        return total_buying_cost