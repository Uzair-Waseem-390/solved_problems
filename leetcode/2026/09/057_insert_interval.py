# Insert Interval
# Difficulty: Medium
# https://leetcode.com/problems/insert-interval/

# Iterate through intervals, adding those that come before, merging overlaps, then adding those that come after.
# This three-phase approach handles all cases efficiently in a single pass.

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        merged_intervals = []
        current_interval_index = 0
        number_of_intervals = len(intervals)

        # Phase 1: Add all intervals that come strictly before newInterval
        while current_interval_index < number_of_intervals and \
              intervals[current_interval_index][1] < newInterval[0]:
            merged_intervals.append(intervals[current_interval_