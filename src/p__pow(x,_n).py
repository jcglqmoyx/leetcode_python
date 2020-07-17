class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        m, result = n, 1
        if m < 0:
            m = -m
        while m > 0:
            if (m & 1) == 1:
                result *= x
            x *= x
            m >>= 1
        return result if n > 0 else 1 / result
