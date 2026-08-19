# Cinema Seat Allocation
# Difficulty: Medium
# https://leetcode.com/problems/cinema-seat-allocation/

# Uses a hash map to store reserved seats for each row, representing seat availability with bitmasks.
# Calculates groups for rows with reservations, then adds two groups for all unreserved rows.
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        row_seat_masks = defaultdict(int)
        for row, seat in reservedSeats:
            row_seat_masks[row] |= (1 << (seat - 1))

        # Masks for the three possible seat blocks (0-indexed bits):
        # Block 1: seats 2,3,4,5 (bits 1,2,3,4)
        left_block_