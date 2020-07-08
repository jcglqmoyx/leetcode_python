# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         d = [0] * 123
#         for c in text:
#             if c in 'balloon':
#                 d[ord(c)] += 1
#         return min(d[ord('b')], d[ord('a')], d[ord('l')] // 2, d[ord('o')] // 2, d[ord('n')])

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count(c) // 'balloon'.count(c) for c in 'balon')
