# Lexicographically Smallest Permutation Greater Than Target
# Difficulty: Medium
# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

# This problem requires finding the lexicographically smallest permutation of `s` that is strictly greater than `target`.
# A greedy approach combined with backtracking-like logic works here: iterate through potential "pivot" positions `i` from left to right.
# At each `i`, try to place a character `c` such that `c > target[i]`. If successful, fill the rest with the smallest available characters and record this candidate.
# If no such `c` exists, or after trying all such `c`, try to match `target[i]` (i.e., `c == target[i]`) and continue to the next position.
# If `target[i]` cannot be matched, it means no permutation starting with the current prefix can be