from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c) + 1)):
            diff = c - i ** 2
            if int(sqrt(diff)) ** 2 == diff:
                return True
        return False
