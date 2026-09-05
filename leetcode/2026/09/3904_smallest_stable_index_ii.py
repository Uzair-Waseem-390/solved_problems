# Smallest Stable Index II
# Difficulty: Medium
# https://leetcode.com/problems/smallest-stable-index-ii/

# Precompute prefix maximums and suffix minimums to efficiently calculate instability score for each index in O(N) time.

class Solution:
    def smallestStableIndex(self, nums: list[int], k: int) -> int:
        nums_length = len(nums)

        prefix_maximums = [0] * nums_length
        prefix_maximums[0] = nums[0]
        for i in range(1, nums_length):
            prefix_maximums[i] = max(prefix_maximums[i-1], nums[i])

        suffix_minimums = [0] * nums_length
        suffix_minimums[nums_length-1] = nums[nums_length-1]
        for i in range(nums_length - 2, -1, -1):
            suffix_minimums[i] = min(suffix_minimums[i+1], nums[i])

        for i in range(nums_length):
            instability_score = prefix_maximums[i] - suffix_minimums[i]
            if instability_score <= k:
                return i
        
        return -1