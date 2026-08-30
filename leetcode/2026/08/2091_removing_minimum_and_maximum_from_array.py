# Removing Minimum and Maximum From Array
# Difficulty: Medium
# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

# Identify min/max values and their indices. Three scenarios for removal: both from front, both from back, or one from each end. Calculate deletions for each and take the minimum.

import math

class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        min_value = math.inf
        max_value = -math.inf
        min_value_index = -1
        max_value_index = -1

        for i in range(n):
            if nums[i] < min_value:
                min_value = nums[i]
                min_value_index = i
            if nums[i] > max_value:
                max_value = nums[i]
                max_value_index = i
        
        left_target_index = min(min_value_index, max_value_index)
        right_target_index = max(min_value_index, max_value_index)

        deletions_both_from_front = right_target_index + 1

        deletions_both_from_back = n - left_target_index

        deletions_one_from_front_one_from_back = (left_target_index + 1) + (n - right_target_index)

        return min(deletions_both_from_front, deletions_both_from_back, deletions_one_from_front_one_from_back)