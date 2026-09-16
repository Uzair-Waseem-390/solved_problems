# Number of Sets of K Non-Overlapping Line Segments
# Difficulty: Medium
# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

# This problem can be solved using dynamic programming.
# Let dp[i][j] be the number of ways to draw exactly j segments using points from 0 to i.
# The transitions involve two cases:
# 1. Not ending any segment at point i: This contributes dp[i-1][j] ways.
# 2. Ending the j-th segment at point i: This segment is [p, i] for some 0 <= p < i.
#    The previous j-1 segments must be formed using points 0 to p.
#    So, we sum dp[p][j-1] for all p from 0 to i-1.
# This sum can be optimized using a prefix sum array (or a running sum