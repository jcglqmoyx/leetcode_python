from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        mi, ma = 10000, 1
        for num in A:
            if num < mi:
                mi = num
            if num > ma:
                ma = num
        return max(ma - mi - 2 * K, 0)
