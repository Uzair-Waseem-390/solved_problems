# Multiply Strings
# Difficulty: Medium
# https://leetcode.com/problems/multiply-strings/

# Simulates long multiplication by hand. Iterate through digits of num1 and num2 from right to left,
# multiplying each pair and adding to the correct positions in a result array, handling carries.
# Finally, convert the digit array to a string, skipping leading zeros.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        len1 = len(num1)
        len2 = len(num2)
        product_digits = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            digit