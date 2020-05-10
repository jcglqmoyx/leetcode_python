from typing import List


# class Solution:
#     def sortArrayByParityII(self, A: List[int]) -> List[int]:
#         result = [0] * len(A)
#         i, j = 0, 1
#         for index in range(0, len(A)):
#             if (index & 1) == 0 and (A[index] & 1) == 0:
#                 result[i] = A[index]
#                 i += 2
#             elif (index & 1) == 1 and (A[index] & 1) == 1:
#                 result[j] = A[index]
#                 j += 2
#             elif (index & 1) == 0:
#                 result[j] = A[index]
#                 j += 2
#             else:
#                 result[i] = A[index]
#                 i += 2
#         return result


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        od = []
        ev = []
        for i in A:
            if i % 2:
                od.append(i)
            else:
                ev.append(i)
        res[0::2] = ev
        res[1::2] = od
        return res
