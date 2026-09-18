# Jump Game
# Difficulty: Medium
# https://leetcode.com/problems/jump-game/

# Greedy approach: work backwards from the target. If an index can reach the current target, that index becomes the new target.
# If index 0 can become the target, then it's possible to reach the end.

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        last_reachable_index = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_reachable_index:
                last_reachable_index = i
        
        return last_reachable_index == 0