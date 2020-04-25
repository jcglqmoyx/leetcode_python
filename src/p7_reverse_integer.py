import sys


class Solution:
    def reverse(self, x: int) -> int:
        isNeg = x < 0
        min = -pow(2, 31)
        max = pow(2, 31) - 1
        num = 0
        if isNeg:
            x = -x
        while x:
            num = (num + x % 10) * 10
            x //= 10
        res = num // 10
        if not isNeg:
            return 0 if res > max else res
        else:
            return 0 if -res < min else -res


print(Solution().reverse(1))
print(Solution().reverse(10))
print(Solution().reverse(1234))
print(Solution().reverse(sys.maxsize))
print(Solution().reverse(-sys.maxsize - 1))
