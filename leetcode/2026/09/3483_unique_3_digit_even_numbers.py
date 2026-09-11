# Unique 3-Digit Even Numbers
# Difficulty: Easy
# https://leetcode.com/problems/unique-3-digit-even-numbers/

# Count digit frequencies and iterate through all possible 3-digit even numbers.
# For each candidate number, verify if its digits can be formed from the available input digits' counts.
# Use a set to collect unique valid numbers and return its size.

import collections

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> int:
        digit_counts = collections.Counter(digits)
        found_numbers = set()

        for num in range(100, 1000, 2):
            hundreds_digit = num // 100
            tens_digit = (num // 10) % 10
            units_digit = num % 10

            temp_counts = collections.Counter([hundreds_digit, tens_digit, units_digit])

            can_form = True
            for digit, count_needed in temp_counts.items():
                if digit_counts[digit] < count_needed:
                    can_form = False
                    break
            
            if can_form:
                found_numbers.add(num)
        
        return len(found_numbers)