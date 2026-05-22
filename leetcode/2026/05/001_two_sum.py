# Two Sum
# Difficulty: Easy
# https://leetcode.com/problems/two-sum/

# Use a hash map to store numbers and their indices, allowing O(1) lookups for complements.
# Iterate once, for each number, check if its complement is already in the map.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Stores numbers seen so far along with their original indices.
        # Key: number, Value: index
        num_map = {} 

        for index, current_num in enumerate(nums):
            complement = target - current_num
            
            # If the complement exists in our map, we've found the pair.
            if complement in num_map:
                # The index of the complement is retrieved from the map,
                # and the current number's index is `index`.
                return [num_map[complement], index]
            
            # If complement not found, add the current number and its index to the map
            # for future lookups.
            num_map[current_num] = index

        # The problem statement guarantees exactly one solution,
        # so this line should theoretically not be reached.
        return []<ctrl63>