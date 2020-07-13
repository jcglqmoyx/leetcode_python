from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        increase = 0
        row, col = [0] * len(grid), [0] * len(grid[0])
        for i in range(len(grid)):
            max_row = 0
            for j in grid[i]:
                if j > max_row:
                    max_row = j
            row[i] = max_row
        for i in range(len(grid[0])):
            max_col = 0
            for j in range(len(grid[i])):
                if grid[j][i] > max_col:
                    max_col = grid[j][i]
            col[i] = max_col
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                increase += min(row[i], col[j]) - grid[i][j]
        return increase
