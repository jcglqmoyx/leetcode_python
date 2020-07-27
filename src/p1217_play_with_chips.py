from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        count_odd = count_even = 0
        for chip in chips:
            if (chip & 1) == 0:
                count_even += 1
            else:
                count_odd += 1
        return min(count_odd, count_even)
