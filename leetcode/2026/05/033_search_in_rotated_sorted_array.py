# Search in Rotated Sorted Array
# Difficulty: Medium
# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Binary search adapted for rotated arrays. The key is to always identify which half (left or right of mid) is sorted
# then check if the target falls within that sorted range. If so, search that half; otherwise, search the other half.
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            # Determine which half is sorted
            if nums[low] <= nums[mid]:  # Left half is sorted
                if nums[low] <= target < nums[mid]:
                    # Target is in the sorted left half
                    high = mid - 1
                else:
                    # Target is in the right half (which might be rotated)
                    low = mid + 1
            else:  # Right half is sorted (nums[low] > nums[mid] implies rotation point is in the left half)
                if nums[mid] < target <= nums[high]:
                    # Target is in the sorted right half
                    low = mid + 1
                else:
                    # Target is in the left half (which might be rotated)
                    high = mid - 1
        
        return -1 # Target was not found