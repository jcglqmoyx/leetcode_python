from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        number = 0
        group = [0] * 60
        for t in time:
            group[t % 60] += 1
        number += group[0] * (group[0] - 1) // 2
        number += group[30] * (group[30] - 1) // 2
        for i in range(1, 30):
            number += group[i] * group[60 - i]
        return number
