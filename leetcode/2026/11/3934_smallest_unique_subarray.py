# Smallest Unique Subarray
# Difficulty: Hard
# https://leetcode.com/problems/smallest-unique-subarray/

# Binary search on the length of the subarray. For a given length, use rolling hash to count frequencies of all subarrays of that length. If any subarray has a frequency of 1, that length is possible.

class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        # Choose a base and a modulus for rolling hash.
        # P should be a prime larger than max(nums[i]). max(nums[i]) is 10^5.
        # M should be a large prime to minimize collisions.
        prime_base = 100003
        modulus = 10**9 + 7

        def check(length