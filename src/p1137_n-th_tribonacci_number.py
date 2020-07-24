class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        zero, first, second, third = 0, 1, 1, 2
        for i in range(3, n + 1):
            third = zero + first + second
            zero = first
            first = second
            second = third
        return third
