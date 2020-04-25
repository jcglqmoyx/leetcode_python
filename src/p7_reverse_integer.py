class Solution:
    def reverse(self, x: int) -> int:
        isNeg = x < 0
        min = -pow(2, 31)
        max = pow(2, 31) - 1
        num = 0
        if isNeg:
            x = -x
        while x:
            last_digit = x % 10
            num = (num + last_digit) * 10
            x //= 10
        res = num // 10
        if not isNeg:
            return 0 if res > max else res
        else:
            return 0 if -res < min else -res