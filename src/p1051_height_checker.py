from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = heights.copy()
        temp.sort()
        count = 0
        for i in range(len(heights)):
            if temp[i] != heights[i]:
                count += 1
        return count
