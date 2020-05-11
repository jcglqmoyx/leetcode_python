from typing import List

'''
This is not a efficient solution. To see the revised version, view the code of the Java implementation 
or Cpp implematation.
'''

# def is_lucky_number(matrix: List[List[int]], i: int, j: int) -> bool:
#     if matrix[i][j] == min(matrix[i]):
#         for k in range(len(matrix)):
#             if matrix[k][j] > matrix[i][j]:
#                 return False
#         return True
#     return False
#
#
# class Solution:
#     def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
#         lucky_numbers = []
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if is_lucky_number(matrix, i, j):
#                     lucky_numbers.append(matrix[i][j])
#         return lucky_numbers
#
#
# m = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
# print(Solution().luckyNumbers(m))


'''
This is the best solution.
'''


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mi = {min(r) for r in matrix}
        ma = {max(r) for r in zip(*matrix)}
        return list(mi & ma)
