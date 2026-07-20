# Shift 2D Grid
# Difficulty: Easy
# https://leetcode.com/problems/shift-2d-grid/

# Treat the 2D grid as a 1D array, perform the shift on the flattened array, then reconstruct the 2D grid.
class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows = len(grid)
        cols = len(grid[0])
        total_grid_size = rows * cols

        flat_list = []
        for r in range(rows):
            for c in range(cols):
                flat_list.append(grid[r][c])

        effective_shifts = k % total_grid_size

        shifted_flat_list = flat_list[-effective_shifts:] + flat_list[:-effective_shifts]

        shifted_grid = [[0] * cols for _ in range(rows)]
        for i in range(total_grid_size):
            r_idx = i // cols
            c_idx = i % cols
            shifted_grid[r_idx][c_idx] = shifted_flat_list[i]

        return shifted_grid