# Candy
# Difficulty: Hard
# https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: list[int]) -> int:
        num_children = len(ratings)
        
        candies = [1] * num_children
        
        # First pass: left to right, ensuring higher rated children get more candies than their left neighbor
        for i in range(1, num_children):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Second pass: right to left, ensuring higher rated children get more candies than their right neighbor
        # We take the maximum to satisfy both left and right conditions
        for i in range(num_children - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
                
        return sum(candies)