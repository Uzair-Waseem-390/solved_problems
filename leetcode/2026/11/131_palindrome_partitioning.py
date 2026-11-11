# Palindrome Partitioning
# Difficulty: Medium
# https://leetcode.com/problems/palindrome-partitioning/

# This problem can be solved using a backtracking approach.
# We recursively explore all possible partitions of the string.
# At each step, we check if a substring is a palindrome, and if so,
# we add it to the current partition and recurse on the remaining string.
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        all_partitions = []
        current_partition = []
        n = len(s)

        def is_palindrome(start_index, end_index):
            while start_index < end_index:
                if s[start_index] != s[end_index]:
                    return False
                start_index += 1
                end_index -= 1
            return True

        def backtrack(start_index):
            if start_index == n:
                all_partitions.append(list(current_partition))
                return

            for end_index in range(start_index, n):
                if is_palindrome(start_index, end_index):
                    current_partition.append(s[start_index : end_index + 1])
                    backtrack(end_index + 1)
                    current_partition.pop()

        backtrack(0)
        return all_partitions