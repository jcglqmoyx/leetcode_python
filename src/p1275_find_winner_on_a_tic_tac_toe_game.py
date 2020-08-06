from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        flag = True
        for move in moves:
            if flag:
                grid[move[0]][move[1]] = 'X'
                flag = False
            else:
                grid[move[0]][move[1]] = 'O'
                flag = True
        if grid[0][0] == grid[0][1] == grid[0][2] != 0 \
                or grid[1][0] == grid[1][1] == grid[1][2] != 0 \
                or grid[2][0] == grid[2][1] == grid[2][2] != 0 \
                or grid[0][0] == grid[1][0] == grid[2][0] != 0 \
                or grid[0][1] == grid[1][1] == grid[2][1] != 0 \
                or grid[0][2] == grid[1][2] == grid[2][2] != 0 \
                or grid[0][0] == grid[1][1] == grid[2][2] != 0 \
                or grid[0][2] == grid[1][1] == grid[2][0] != 0:
            return 'A' if len(moves) % 2 == 1 else 'B'
        if len(moves) < 9:
            return 'Pending'
        else:
            return 'Draw'
