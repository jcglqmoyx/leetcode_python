from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        num = 0
        for n in arr1:
            flag = True
            for e in arr2:
                if abs(n - e) <= d:
                    flag = False
                    break
            if flag:
                num += 1
        return num
