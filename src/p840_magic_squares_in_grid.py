from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        number = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if grid[i + 1][j + 1] == 5 and self.has_all_numbers(i, j, grid):
                    if (grid[i][j] + grid[i][j + 1] + grid[i][j + 2] == 15 and
                            grid[i][j] + grid[i + 1][j] + grid[i + 2][j] == 15 and
                            grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2] == 15 and
                            grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2] == 15 and
                            grid[i][j + 1] + grid[i + 2][j + 1] == 10 and grid[i + 1][j] + grid[i + 1][j + 2] == 10 and
                            grid[i][j] + grid[i + 2][j + 2] == 10 and grid[i][j + 2] + grid[i + 2][j] == 10):
                        number += 1
        return number

    def has_all_numbers(self, i: int, j: int, grid: List[List[int]]) -> bool:
        arr = [0] * 16
        for m in range(i, i + 3):
            for n in range(j, j + 3):
                arr[grid[m][n]] = 1
        for index in range(1, 10):
            if arr[index] != 1:
                return False
        return True
