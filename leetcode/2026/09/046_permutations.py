# Permutations
# Difficulty: Medium
# https://leetcode.com/problems/permutations/

# Standard backtracking approach to explore all possible paths (permutations) by choosing one element at a time, marking it as used, and then unmarking it (backtracking).

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        all_permutations = []
        n = len(nums)
        used_elements = [False] * n

        def backtrack(current_permutation):
            if len(current_permutation) == n:
                all_permutations.append(list(current_permutation))
                return

            for i in range(n):
                if not used_elements[i]:
                    current_permutation.append(nums[i])
                    used_elements[i] = True
                    backtrack(current_permutation)
                    used_elements[i] = False
                    current_permutation.pop()

        backtrack([])
        return all_permutations