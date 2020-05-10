# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         i, j, carry = len(num1) - 1, len(num2) - 1, 0
#         result = ''
#         while i >= 0 or j >= 0:
#             if i >= 0 and j >= 0:
#                 x = ord(num1[i]) - 48
#                 y = ord(num2[j]) - 48
#                 sum = x + y + carry
#                 i -= 1
#                 j -= 1
#             elif i >= 0:
#                 x = ord(num1[i]) - 48
#                 sum = x + carry
#                 i -= 1
#             else:
#                 y = ord(num2[j]) - 48
#                 sum = y + carry
#                 j -= 1
#             result += str(sum % 10)
#             carry = sum // 10
#         if carry:
#             result += '1'
#         return result[::-1]


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))
