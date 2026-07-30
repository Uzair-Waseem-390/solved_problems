# Minimum Number of Pushes to Type Word I
# Difficulty: Easy
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

# The problem is a greedy distribution problem. To minimize pushes,
# we should assign characters to 1-push slots first, then 2-push slots, and so on.
# There are 8 keys, so we can assign 8 characters at 1 push each, then 8 at 2 pushes each, etc.
class Solution:
    def minimumPushes(self, word: str) -> int:
        num_letters = len(word)
        total_pushes = 0
        current_push_cost = 1
        keys_available = 8

        while num_letters > 0:
            letters_at_this_level = min(num_letters, keys_available)
            total_pushes += letters_at_this_level * current_push_cost
            num_letters -= letters_at_this_level
            current_push_cost += 1
        
        return total_pushes