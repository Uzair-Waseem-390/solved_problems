# Earliest Finish Time for Land and Water Rides II
# Difficulty: Medium
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

import bisect

class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        # This problem can be solved by sorting each ride category by start time.
        # Then, for each ride in the first category, we binary search the second category to find optimal pairings.
        # Two cases for the second ride: it opens before/at the first ride's finish time, or it opens later.
        # Precomputing prefix minimum durations and suffix minimum finish times for the second category allows O(log M) lookup.
        # This process is repeated for both possible orders (land then water, water then land).