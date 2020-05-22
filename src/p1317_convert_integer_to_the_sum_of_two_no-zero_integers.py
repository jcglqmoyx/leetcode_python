from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if self.is_no_zero_integer(i) and self.is_no_zero_integer(n - i):
                return [i, n - i]
        return []

    def is_no_zero_integer(self, n: int) -> bool:
        while n:
            last_digit = n % 10
            if last_digit == 0:
                return False
            n //= 10
        return True
