# class Solution:
#     def reverseOnlyLetters(self, S: str) -> str:
#         result = list(S)
#         low, high = 0, len(result) - 1
#         while low < high:
#             while low < high and not result[low].isalpha():
#                 low += 1
#             while low < high and not result[high].isalpha():
#                 high -= 1
#             temp = result[low]
#             result[low] = result[high]
#             result[high] = temp
#             low += 1
#             high -= 1
#         return ''.join(result)


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        result = list(S)
        low, high = 0, len(S) - 1
        while low < high:
            if not S[low].isalpha():
                low += 1
            elif not S[high].isalpha():
                high -= 1
            else:
                result[low], result[high] = result[high], result[low]
                low, high = low + 1, high - 1
        return ''.join(result)
