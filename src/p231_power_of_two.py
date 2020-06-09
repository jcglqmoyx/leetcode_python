# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n < 1:
#             return False
#         while n % 2 == 0:
#             n >>= 1
#         return n == 1


# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         return (n & (-n)) == n


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return (n & (n - 1)) == 0
