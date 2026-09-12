# Maximum Score of Non-overlapping Intervals
# Difficulty: Hard
# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

# This problem can be solved using dynamic programming.
# Sort intervals by their right boundaries to facilitate finding non-overlapping previous intervals using binary search.
# The DP state `dp[k][i]` stores the maximum score and lexicographically smallest indices for choosing `k` intervals
# from the first `i` sorted intervals, where the `i`-th interval is *not necessarily* chosen.
# When considering interval `i` for `k` intervals, we either don't choose it (taking `dp[k][i-1]`)
# or we choose it, in which case we look for the best `k-1` intervals that end before `intervals[i].left`.
# The lexicographical comparison logic is critical when scores are equal.

class