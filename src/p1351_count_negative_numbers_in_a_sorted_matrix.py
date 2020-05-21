from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[i]) - 1, -1, -1):
                if grid[i][j] >= 0:
                    count += len(grid[i]) - j - 1
                    break
                elif j == 0:
                    count += len(grid[i])
        return count
