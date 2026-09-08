# Count Commas in Range
# Difficulty: Easy
# https://leetcode.com/problems/count-commas-in-range/

# Numbers less than 1000 have no commas. For n up to 10^5, any number with commas will only have one comma.
# The solution counts how many numbers in the range [1, n] are 1000 or greater.
class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        else:
            return n - 1000 + 1