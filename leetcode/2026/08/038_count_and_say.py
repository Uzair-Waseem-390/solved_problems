# Count and Say
# Difficulty: Medium
# https://leetcode.com/problems/count-and-say/

# The problem requires generating the nth term of a sequence where each term is the run-length encoding of the previous one. An iterative approach works well: start with "1" and repeatedly apply a helper function to generate the next term until the nth term is reached.

class Solution:
    def countAndSay(self, n: int) -> str:
        
        def generate_next_sequence(previous_sequence: str) -> str:
            if not previous_sequence:
                return ""

            next_sequence_parts = []
            index = 0
            while index < len(previous_sequence):
                current_digit = previous_sequence[index]
                count = 0
                
                # Count consecutive occurrences of current_digit
                scanner_index = index
                while scanner_index < len(previous_sequence) and previous_sequence[scanner_index] == current_digit:
                    count += 1
                    scanner_index += 1
                
                next_sequence_parts.append(str(count))
                next_sequence_parts.append(current_digit)
                
                # Move the main index to the position after the counted group
                index = scanner_index
            
            return "".join(next_sequence_parts)

        current_sequence = "1"
        for _ in range(1, n):
            current_sequence = generate_next_sequence(current_sequence)
        
        return current_sequence