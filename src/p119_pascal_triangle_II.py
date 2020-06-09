from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(0, rowIndex + 1):
            result.append(self.combination(rowIndex, i))
        return result

    def combination(self, n: int, r: int) -> int:
        if r > n // 2:
            return self.combination(n, n - r)
        if r == 0:
            return 1
        result, r_value = 1, r
        for i in range(0, r_value):
            result *= n
            result /= r
            n -= 1
            r -= 1
        return int(round(result))
