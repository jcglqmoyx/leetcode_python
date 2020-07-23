from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num
        diff = bitmask & (-bitmask)
        x = 0
        for num in nums:
            if num & diff != 0:
                x ^= num
        return [x, bitmask ^ x]
