from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        result = []
        i = len(A) - 1
        sum = carry = 0
        while i >= 0 or K > 0:
            if i >= 0 and K > 0:
                sum = A[i] + K % 10 + carry
                i -= 1
                K //= 10
            elif i >= 0:
                sum = A[i] + carry
                i -= 1
            else:
                sum = K % 10 + carry
                K //= 10
            carry = sum // 10
            result.insert(0, sum % 10)
        if carry:
            result.insert(0, 1)
        return result
