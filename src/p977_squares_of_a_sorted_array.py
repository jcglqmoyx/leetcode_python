from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # low, high = 0, len(A) - 1
        # ret = []
        # while low <= high:
        #     if abs(A[low]) < abs(A[high]):
        #         ret.insert(0, pow(A[high], 2))
        #         high -= 1
        #     else:
        #         ret.insert(0, pow(A[low], 2))
        #         low += 1
        # return ret
        return sorted(list(i * i for i in A))


print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
print(Solution().sortedSquares([-7, -3, 2, 3, 11]))
