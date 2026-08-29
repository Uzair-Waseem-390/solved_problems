# Make Lexicographically Smallest Array by Swapping Elements
# Difficulty: Medium
# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

# Use Union-Find to group elements that can be swapped.
# Sort (value, original_index) pairs to easily find adjacent values within the limit and union their original indices.
# Then, for each connected component, sort its values and its original indices, and assign the sorted values to the sorted indices.

import collections

class Solution:
    def makeLexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)

        class DSU:
            def __init__(self, size):
                self.parent = list(range(size))

            def find(self, i):
                if self.parent[i] == i:
                    return i
                self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def union(self, i, j):
                root_i = self.find(i)
                root_j = self.find(j)
                if root_i != root_j:
                    self.parent[root_j] = root_i
                    return True
                return False

        dsu = DSU(n)

        indexed_nums = []
        for i in range(n):
            indexed_nums.append((nums[i], i))
        
        indexed_nums.sort()

        for i in range(1, n):
            if indexed_nums[i][0] - indexed_nums[i-1][0] <= limit:
                dsu.union(indexed_nums[i][1], indexed_nums[i-1][1])
        
        components = collections.defaultdict(lambda: {'values': [], 'indices': []})
        for i in range(n):
            root = dsu.find(i)
            components[root]['values'].append(nums[i])
            components[root]['indices'].append(i)
        
        result = [0] * n
        for root in components:
            current_values = components[root]['values']
            current_indices = components[root]['indices']
            
            current_values.sort()
            current_indices.sort()
            
            for i in range(len(current_values)):
                result[current_indices[i]] = current_values[i]
        
        return result