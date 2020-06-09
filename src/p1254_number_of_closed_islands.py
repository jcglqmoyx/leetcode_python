from typing import List


class Solution:
    count = 0

    def closedIsland(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    if self.dfs(grid, i, j):
                        self.count += 1
        return self.count

    def dfs(self, grid: List[List[int]], i: int, j: int) -> bool:
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[i]):
            return False
        if grid[i][j] == 1:
            return True
        grid[i][j] = 1
        a = self.dfs(grid, i - 1, j)
        b = self.dfs(grid, i + 1, j)
        c = self.dfs(grid, i, j - 1)
        d = self.dfs(grid, i, j + 1)
        return a and b and c and d
