from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a = sum_b = 0
        for a in A:
            sum_a += a
        for b in B:
            sum_b += b
        diff = sum_a - sum_b
        for a in A:
            if a - diff // 2 in B:
                return [a, a - diff // 2]
        return []
