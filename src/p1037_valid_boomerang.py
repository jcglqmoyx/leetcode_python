from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a = points[0]
        b = points[1]
        c = points[2]
        return (b[1] - a[1]) * (c[0] - b[0]) != (c[1] - b[1]) * (b[0] - a[0])
