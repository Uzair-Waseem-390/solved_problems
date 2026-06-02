# 3Sum Closest
# Difficulty: Medium
# https://leetcode.com/problems/3sum-closest/

# Sort the array first, then iterate with a fixed element and use two pointers for the remaining pair.
# Update the closest sum found so far based on absolute difference from the target.

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        num_count = len(nums)
        
        # Initialize closest_sum with the sum of the first three elements
        # This is safe because constraints guarantee num_count >= 3
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(num_count - 2):
            left_pointer = i + 1
            right_pointer = num_count - 1

            while left_pointer < right_pointer:
                current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]

                if current_sum == target:
                    return target
                
                # Check if current_sum is closer to target than closest_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left_pointer += 1
                else: # current_sum > target
                    right_pointer -= 1
        
        return closest_sum