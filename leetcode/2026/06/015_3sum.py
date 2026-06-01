# 3Sum
# Difficulty: Medium
# https://leetcode.com/problems/3sum/

# Sort the array first to enable the two-pointer approach for the 2-sum subproblem.
# Handle duplicates by skipping elements that are the same as the previous one.
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return triplets