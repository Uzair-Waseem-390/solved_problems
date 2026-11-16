# Word Break II
# Difficulty: Hard
# https://leetcode.com/problems/word-break-ii/

# This problem is a classic application of backtracking combined with memoization (dynamic programming).
# We explore all possible ways to break the string into dictionary words, storing results for substrings
# to avoid redundant computations, which is essential given the small string length constraint.

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def find_sentences(start_index: int) -> List[str]:
            if start_index == len(s):
                return [""]

            if start_index in memo:
                return memo[start_index]

            possible_sentences = []
            for end_index in range(start_index + 1, len(s) + 1):
                current_word = s[start_index:end_index]
                if current_word in word_set:
                    remaining_sentences = find_sentences(end_index)
                    for sentence_suffix in remaining_sentences:
                        if sentence_suffix:
                            possible_sentences.append(current_word + " " + sentence_suffix)
                        else:
                            possible_sentences.append(current_word)
            
            memo[start_index] = possible_sentences
            return possible_sentences

        return find_sentences(0)