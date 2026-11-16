# Calculate Digit Sum of a String
# Difficulty: Easy
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/

# Simulate the process round by round until the string length is no longer greater than k.
# In each round, divide the string into k-sized groups, calculate the sum of digits for each group,
# convert sums back to strings, and then merge them to form the new string for the next round.

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_round_parts = []
            
            for i in range(0, len(s), k):
                current_group = s[i : i + k]
                
                group_digit_sum = 0
                for digit_char in current_group:
                    group_digit_sum += int(digit_char)
                
                next_round_parts.append(str(group_digit_sum))
            
            s = "".join(next_round_parts)
            
        return s