# Find the Distance Value Between Two Arrays
# Difficulty: Easy
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

# The problem asks to count elements in arr1 that are "far" from all elements in arr2.
# This can be directly translated into nested loops: for each element in arr1, iterate through arr2 to check the distance condition.
# The given constraints (array lengths up to 500) allow for this O(N*M) approach, making it straightforward to implement.

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        distance_value_count = 0
        for num1 in arr1:
            is_far_from_all_arr2 = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    is_far_from_all_arr2 = False
                    break
            if is_far_from_all_arr2:
                distance_value_count += 1
        return distance_value_count