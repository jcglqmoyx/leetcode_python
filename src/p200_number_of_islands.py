from typing import List


class Solution:
    count = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    self.count += 1
        return self.count

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[i]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
