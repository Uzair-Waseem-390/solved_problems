# Longest Consecutive Sequence
# Difficulty: Medium
# https://leetcode.com/problems/longest-consecutive-sequence/

# Using a hash set to store all numbers allows O(1) average time lookups.
# Iterate through each number, only starting a new sequence check if `num - 1` is not present in the set.
# This ensures each potential number in a sequence is visited a constant number of times overall, leading to O(N) complexity.

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest_sequence_length = 0

        for num in nums:
            # Check if current_num is the start of a sequence
            # i.e., current_num - 1 is not in the set
            if (num - 1) not in num_set:
                current_num = num
                current_sequence_length = 1

                # Extend the sequence upwards
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_sequence_length += 1
                
                longest_sequence_length = max(longest_sequence_length, current_sequence_length)
        
        return longest_sequence_length