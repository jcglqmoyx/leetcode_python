from typing import List


# class Solution:
#     def repeatedNTimes(self, A: List[int]) -> int:
#         map = {}
#         for num in A:
#             if num in map:
#                 map[num] += 1
#             else:
#                 map[num] = 1
#         for key, value in map.items():
#             if value == len(A) // 2:
#                 return key
#         return -1

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(2, len(A)):
            if A[i] == A[i - 1] or A[i] == A[i - 2]:
                return A[i]
        return A[0]
