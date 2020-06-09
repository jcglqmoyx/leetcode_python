from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = 0
        for num in nums:
            n ^= num
        return n
