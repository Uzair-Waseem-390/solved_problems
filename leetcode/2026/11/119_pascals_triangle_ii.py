# Pascal's Triangle II
# Difficulty: Easy
# https://leetcode.com/problems/pascals-triangle-ii/

# Generate the row iteratively, building upon the previous state.
# We can optimize space to O(rowIndex) by modifying the list in-place,
# appending the trailing '1' and then summing elements from right to left
# to ensure we use values from the previous "conceptual" row before they are updated.
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        
        for i in range(1, rowIndex + 1):
            row.append(1)
            
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j-1]
                
        return row