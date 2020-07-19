from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        store = 0
        for i in range(len(A) - 1):
            diff = self.cmp(A[i], A[i + 1])
            if diff != 0:
                if diff != store and store != 0:
                    return False
                store = diff
        return True

    def cmp(self, a: int, b: int) -> int:
        if a == b:
            return 0
        else:
            return 1 if a > b else -1
