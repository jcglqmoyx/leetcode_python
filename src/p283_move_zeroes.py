from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                while nums[i] != 0:
                    i += 1
                    if i >= len(nums):
                        return
                if i < j:
                    nums[i] = nums[j]
                    nums[j] = 0
