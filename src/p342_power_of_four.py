# class Solution:
#     def isPowerOfFour(self, num: int) -> bool:
#         if num < 1:
#             return False
#         while num > 1:
#             if num % 4 != 0:
#                 return False
#             num >>= 2
#         return True

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num and (num & (num - 1)) == 0 and num % 3 == 1
