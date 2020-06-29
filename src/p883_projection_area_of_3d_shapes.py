from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area, length = 0, len(grid)
        for i in range(length):
            max1 = max2 = 0
            for j in range(length):
                if grid[i][j] != 0:
                    area += 1
                max1 = max(max1, grid[i][j])
                max2 = max(max2, grid[j][i])
            area += max1 + max2
        return area
