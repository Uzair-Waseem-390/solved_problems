# Maximize Sum of Squares of Digits
# Difficulty: Medium
# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

# Greedy approach: to maximize sum of squares, we want digits to be as far apart as possible (0s and 9s).
# To maximize the number itself, we want larger digits in the leftmost positions.
# These two goals align, so we greedily fill digits from left to right, picking the largest possible valid digit.
# A digit is valid if it's within [0, 9] (or [1, 9] for the first digit of a multi-digit number), and
# if the remaining sum can be formed by the remaining digits (i.e., remaining_sum is between 0 and 9 * remaining_digits).

class Solution:
    def maximizeSumOfSquaresOfDigits(self, num: int, sum: int)