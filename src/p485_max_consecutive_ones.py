from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = 0
        max_length = 0
        for i in nums:
            if i:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 0
        max_length = max(max_length, length)
        return max_length
