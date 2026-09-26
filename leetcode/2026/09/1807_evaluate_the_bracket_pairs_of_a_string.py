# Evaluate the Bracket Pairs of a String
# Difficulty: Medium
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

# Use a hash map to store knowledge for O(1) lookups, then iterate through the string
# using a state variable to build the result and current key.

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_map = {}
        for key_val_pair in knowledge:
            knowledge_map[key_val_pair[0]] = key_val_pair[1]

        result_parts = []
        current_key_builder = []
        is_parsing_key = False

        for char in s:
            if char == '(':
                is_parsing_key = True
                current_key_builder = []
            elif char == ')':
                is_parsing_key = False
                key = "".join(current_key_builder)
                value = knowledge_map.get(key, "?")
                result_parts.append(value)
            else:
                if is_parsing_key:
                    current_key_builder.append(char)
                else:
                    result_parts.append(char)
        
        return "".join(result_parts)