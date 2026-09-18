# Merge Intervals
# Difficulty: Medium
# https://leetcode.com/problems/merge-intervals/

# Sort intervals by their start times. Iterate through sorted intervals, merging current interval with the last one if they overlap, otherwise adding it as a new non-overlapping interval.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        merged_intervals = []

        for current_interval in intervals:
            if not merged_intervals or current_interval[0] > merged_intervals[-1][1]:
                merged_intervals.append(current_interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], current_interval[1])
        
        return merged_intervals