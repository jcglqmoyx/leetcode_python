# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         ret, l_count, r_count = 0, 0, 0
#         for ch in s:
#             if ch == 'L':
#                 l_count += 1
#             else:
#                 r_count += 1
#             if l_count == r_count:
#                 ret += 1
#         return ret

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        d = {'r': 0, 'L': 0, 'R': 0}
        for i in range(len(s)):
            if s[i] == 'L':
                d['L'] += 1
            if s[i] == 'R':
                d['R'] += 1
            if d['L'] == d['R']:
                d['r'] += 1
        return d['r']