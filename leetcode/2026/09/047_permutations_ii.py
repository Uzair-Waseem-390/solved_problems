# Permutations II
# Difficulty: Medium
# https://leetcode.com/problems/permutations-ii/

# Backtracking with sorting to handle duplicates efficiently.
# Sorting groups identical elements together, which allows us to use a simple check
# (if current element is same as previous AND previous was not used) to skip redundant branches.
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()  # Sort the input array to group duplicate numbers
        
        # used_indices tracks which elements from the original nums (by their index)
        # have been included in the current permutation path.
        used_indices = [False] * len(nums)
        
        def backtrack(current_permutation):
            # Base case: if the current permutation is complete