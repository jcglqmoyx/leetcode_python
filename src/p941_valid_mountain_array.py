from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        index = 0
        while index < len(A) - 1 and A[index] < A[index + 1]:
            index += 1
        if index == 0 or index == len(A) - 1:
            return False
        while index < len(A) - 1:
            if A[index] <= A[index + 1]:
                return False
            index += 1
        return True
