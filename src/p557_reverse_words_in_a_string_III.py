# class Solution:
#     def reverseWords(self, s: str) -> str:
#         result = ''
#         words = s.split(' ')
#         for word in words:
#             for i in range(len(word) - 1, -1, -1):
#                 result += word[i]
#             result += ' '
#         return result[:-1]


class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        words = s.split()
        for word in words:
            result.append(word[::-1])
        return ' '.join(result)
