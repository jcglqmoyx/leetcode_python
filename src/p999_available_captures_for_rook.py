from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    for a in range(i - 1, -1, -1):
                        if board[a][j] != '.':
                            if board[a][j] == 'p':
                                count += 1
                                break
                            else:
                                break
                    for a in range(i + 1, len(board)):
                        if board[a][j] != '.':
                            if board[a][j] == 'p':
                                count += 1
                                break
                            else:
                                break
                    for a in range(j - 1, -1, -1):
                        if board[i][a] != '.':
                            if board[i][a] == 'p':
                                count += 1
                                break
                            else:
                                break
                    for a in range(j + 1, len(board[0])):
                        if board[i][a] != '.':
                            if board[i][a] == 'p':
                                count += 1
                                break
                            else:
                                break
                    break
        return count
