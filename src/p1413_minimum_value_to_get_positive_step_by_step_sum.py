from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum, min = 0, 10000
        for num in nums:
            sum += num
            if sum < min:
                min = sum
        result = 1 - min
        return max(result, 1)
