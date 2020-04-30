from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        flag, count = 0, 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[flag] = nums[i]
                flag += 1
                count += 1
        for i in range(flag, len(nums)): nums[flag] = 0
        return count