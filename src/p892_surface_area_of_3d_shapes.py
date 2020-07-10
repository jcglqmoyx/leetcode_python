from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surface_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                surface_area += grid[i][j] * 6
                if grid[i][j] > 1:
                    surface_area -= (grid[i][j] - 1) * 2
        for i in range(len(grid)):
            for j in range(len(grid[0]) - 1):
                surface_area -= min(grid[i][j], grid[i][j + 1]) * 2
        for i in range(len(grid) - 1):
            for j in range(len(grid[0])):
                surface_area -= min(grid[i][j], grid[i + 1][j]) * 2
        return surface_area
