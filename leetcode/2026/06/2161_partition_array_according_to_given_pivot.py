# Partition Array According to Given Pivot
# Difficulty: Medium
# https://leetcode.com/problems/partition-array-according-to-given-pivot/

# Create three separate lists for elements less than, equal to, and greater than the pivot.
# Iterate through the input array once, appending elements to the appropriate list to maintain relative order.
# Concatenate the three lists in the required order to form the final result.
class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less_than_pivot_elements = []
        equal_to_pivot_elements = []
        greater_than_pivot_elements = []

        for number in nums:
            if number < pivot:
                less_than_pivot_elements.append(number)
            elif number == pivot:
                equal_to_pivot_elements.append(number)
            else:
                greater_than_pivot_elements.append(number)
        
        return less_than_pivot_elements + equal_to_pivot_elements + greater_than_pivot_elements