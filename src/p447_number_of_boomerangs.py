from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        pass

    def square_of_distance(self, a: List[int], b: List[int]) -> int:
        return pow(a[0] - b[0], 2) - pow(a[1] - b[1], 2)
