# Count Subarrays With Majority Element II
# Difficulty: Hard
# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

# The problem can be transformed into counting subarrays with a positive sum.
# Assign 1 to target elements and -1 to others.
# Then, use prefix sums: `sum(arr[i..j]) > 0` is equivalent to `prefix_sum[j+1] > prefix_sum[i]`.
# This can be efficiently solved using a Fenwick tree (BIT) after shifting values to be non-negative.

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, index, delta):
        index += 1
        while index <= self.size:
            self.tree[