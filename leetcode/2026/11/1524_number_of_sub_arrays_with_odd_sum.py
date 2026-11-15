# Number of Sub-arrays With Odd Sum
# Difficulty: Medium
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

# The problem asks for subarrays with an odd sum.
# We can use prefix sums to solve this. A subarray sum arr[j...k] is prefix_sum[k] - prefix_sum[j-1].
# For this difference to be odd, one prefix sum must be odd and the other even.
# We iterate through the array, maintaining current prefix sum and counts of even/odd prefix sums encountered so far.
# If the current prefix sum is odd, it pairs with all previously encountered even prefix sums to form an odd-sum subarray.
# If the current prefix sum is even, it pairs with all previously encountered odd prefix sums to form an odd-sum subarray.
# Remember to initialize the count of even prefix sums to 1 to account for the empty prefix sum (0).

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        
        even_prefix_sums_count = 1 
        odd_prefix_sums_count = 0 
        
        current_prefix_sum = 0
        total_odd_sum_subarrays = 0
        
        for number in arr:
            current_prefix_sum += number
            
            if current_prefix_sum % 2 == 1:
                total_odd_sum_subarrays = (total_odd_sum_subarrays + even_prefix_sums_count) % MOD
                odd_prefix_sums_count += 1
            else:
                total_odd_sum_subarrays = (total_odd_sum_subarrays + odd_prefix_sums_count) % MOD
                even_prefix_sums_count += 1
                
        return total_odd_sum_subarrays