from typing import List


class CustomFunction:
    def f(self, x, y):
        pass


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1, 1000):
            for y in range(1, 1000):
                result = customfunction.f(x, y)
                if result == z:
                    ans.append([x, y])
                elif result > z:
                    break
        return ans
