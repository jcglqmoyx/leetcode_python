from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count, overlaps = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    count += 1
                    overlaps += self.overlap(grid, i, j)
        return count * 4 - overlaps

    def overlap(self, grid: List[List[int]], i: int, j: int) -> int:
        result = 0
        if i and grid[i - 1][j]:
            result += 1
        if i < len(grid) - 1 and grid[i + 1][j]:
            result += 1
        if j and grid[i][j - 1]:
            result += 1
        if j < len(grid[i]) - 1 and grid[i][j + 1]:
            result += 1
        return result
