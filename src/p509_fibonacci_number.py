# class Solution:
#     def fib(self, N: int) -> int:
#         if N <= 1:
#             return N
#         if N == 2:
#             return 1
#         first, second, third = 1, 1, 2
#         for i in range(3, N + 1):
#             third = first + second
#             first = second
#             second = third
#         return third


class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        a, b = 0, 1
        for _ in range(N - 1):
            c = a + b
            a = b
            b = c
        return b


print(Solution().fib(2))
print(Solution().fib(3))
print(Solution().fib(4))
