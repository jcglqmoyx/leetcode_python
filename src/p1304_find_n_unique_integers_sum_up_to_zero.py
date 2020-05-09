from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [0] * n
        if n & 1:
            index = 1
            for i in range(1, n // 2 + 1):
                result[index] = i
                index += 1
                result[index] = -i
                index += 1
        else:
            index = 0
            for i in range(1, n // 2 + 1):
                result[index] = i
                index += 1
                result[index] = -i
                index += 1
        return result
