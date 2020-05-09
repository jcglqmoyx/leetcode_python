from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        low, high = 0, len(A) - 1
        while low < high:
            while A[low] % 2 == 0 and low < high:
                low += 1
            while A[high] % 2 == 1 and low < high:
                high -= 1
            temp = A[low]
            A[low] = A[high]
            A[high] = temp
        return A
