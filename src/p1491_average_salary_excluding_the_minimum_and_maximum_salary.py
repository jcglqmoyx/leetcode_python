from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        min, max, sum = 1000000, 1000, 0
        for s in salary:
            if s < min:
                min = s
            if s > max:
                max = s
            sum += s
        return (sum - min - max) / (len(salary) - 2)
