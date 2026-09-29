# Plus One
# Difficulty: Easy
# https://leetcode.com/problems/plus-one/

# Iterate from the least significant digit, handling carries.
# If a digit is less than 9, increment and return. If it's 9, set to 0 and carry over.
# If all digits were 9s, prepend a 1 to the resulting array of zeros.
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num_digits = len(digits)

        for i in range(num_digits - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        # If we reach here, it means all digits were 9s (e.g., [9,9,9])
        # So we need to prepend a 1 and all existing digits are now 0s
        return [1] + digits