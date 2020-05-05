# from curses.ascii import isalnum
#
#
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         if not s:
#             return True
#         string = ''
#         for c in s:
#             if isalnum(c):
#                 string += c
#         string = string.lower()
#         low, high = 0, len(string) - 1
#         while low < high:
#             if string[low] != string[high]:
#                 return False
#             low += 1
#             high -= 1
#         return True


import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '').lower()
        for i in string.punctuation:
            s = s.replace(i, '')
        return s == s[::-1]
