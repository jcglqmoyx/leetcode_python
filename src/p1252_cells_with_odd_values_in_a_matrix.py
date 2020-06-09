from typing import List


# class Solution:
#     def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
#         count = 0
#         matrix = [[0] * m for i in range(n)]
#         for indice in indices:
#             for i in range(m):
#                 matrix[indice[0]][i] += 1
#             for j in range(n):
#                 matrix[j][indice[1]] += 1
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 matrix[i][j] >>= 1
#                 if matrix[i][j] % 2 == 1:
#                     count += 1
#         return count

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows, cols = [0] * n, [0] * m
        for index in indices:
            rows[index[0]] ^= 1
            cols[index[1]] ^= 1
        odd_rows = odd_cols = 0
        for i in range(n):
            odd_rows += rows[i]
        for j in range(m):
            odd_cols += cols[j]
        return odd_rows * (m - odd_cols) + odd_cols * (n - odd_rows)
