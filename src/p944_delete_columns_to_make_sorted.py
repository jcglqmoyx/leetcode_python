from typing import List


# class Solution:
#     def minDeletionSize(self, A: List[str]) -> int:
#         columns = 0
#         for i in range(len(A[0])):
#             for j in range(len(A) - 1):
#                 if ord(A[j][i]) > ord(A[j + 1][i]):
#                     columns += 1
#                     break
#         return columns

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        for i in zip(*A):
            if sorted(i) != list(i):
                count += 1
        return count
