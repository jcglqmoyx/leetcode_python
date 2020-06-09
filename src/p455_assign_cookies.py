from typing import *


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        i, j = len(g) - 1, len(s) - 1
        g.sort()
        s.sort()
        while j >= 0:
            while i >= 0 and g[i] > s[j]:
                i -= 1
            if i >= 0:
                count += 1
                i -= 1
            j -= 1
        return count
