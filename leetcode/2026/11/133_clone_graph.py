# Clone Graph
# Difficulty: Medium
# https://leetcode.com/problems/clone-graph/

# Use DFS with a hash map to store already cloned nodes.
# The map prevents cycles and re-cloning, mapping original nodes to their copies.
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloned_map = {}

        def dfs_clone(original_node):
            if original_node in cloned_map:
                return cloned_map[original_node]

            new_clone = Node(original_node.val)
            cloned_map[original_node] = new_clone

            for neighbor in original_node.neighbors:
                new_clone.neighbors.append(dfs_clone(neighbor))

            return new_clone

        return dfs_clone(node)