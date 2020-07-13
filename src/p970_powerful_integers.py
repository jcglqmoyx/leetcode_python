from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        for i in range(20):
            for j in range(20):
                z = x ** i + y ** j
                if z <= bound:
                    result.add(z)
                else:
                    break
        return list(result)
