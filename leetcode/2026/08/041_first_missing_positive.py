# First Missing Positive
# Difficulty: Hard
# https://leetcode.com/problems/first-missing-positive/

# The problem requires O(n) time and O(1) space, suggesting an in-place modification approach.
# We can use the array itself as a hash map: try to place each number `k` at index `k-1`.
# After placement, iterate to find the first index `i` where `nums[i]` is not `i+1`.
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        current_index = 0
        while current_index < n:
            value_at_current_index = nums[current_index]
            target_index_for_value = value_at_current_index - 1