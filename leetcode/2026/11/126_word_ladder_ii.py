# Word Ladder II
# Difficulty: Hard
# https://leetcode.com/problems/word-ladder-ii/

# BFS to find shortest path lengths to all reachable words and build a graph of valid transitions, then DFS to reconstruct all paths of that shortest length.

import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        queue = collections.deque([beginWord])
        distances = {beginWord: 0}
        adj_graph = collections.defaultdict(list)
        
        found_end = False
        
        # BFS to build the graph and find shortest distances
        while queue:
            level_