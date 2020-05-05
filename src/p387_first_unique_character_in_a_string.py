# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - 97] += 1
#         for i in range(len(s)):
#             if count[ord(s[i]) - 97] == 1:
#                 return i
#         return -1


import string


class Solution:
    def firstUniqChar(self, s: str) -> int:
        fc = len(s)
        for c in string.ascii_lowercase:
            left = s.find(c)
            if left != -1 and left == s.rfind(c):
                fc = min(left, fc)
        return fc if fc != len(s) else -1
