# Subarrays Distinct Element Sum of Squares I
# Difficulty: Easy
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

# Iterate through all possible subarrays using nested loops. For each subarray, maintain a set to count distinct elements, then square and sum.
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum_of_squares = 0

        for start_index in range(n):
            current_distinct_elements = set()
            for end_index in range(start_index, n):
                current_distinct_elements.add(nums[end_index])
                distinct_count = len(current_distinct_elements)
                total_sum_of_squares += distinct_count * distinct_count
        
        return total_sum_of_squares