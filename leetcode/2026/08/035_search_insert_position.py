# Search Insert Position
# Difficulty: Easy
# https://leetcode.com/problems/search-insert-position/

# Binary search is the optimal approach for sorted arrays with O(log n) complexity requirement.
# The `low` pointer will correctly indicate the insertion position after the loop terminates.
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return low