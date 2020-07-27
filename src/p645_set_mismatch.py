from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        m = [0] * (len(nums) + 1)
        for num in nums:
            m[num] += 1
        first = second = 0
        for i in range(1, len(m)):
            if m[i] == 2:
                first = i
            if m[i] == 0:
                second = i
        return [first, second]
