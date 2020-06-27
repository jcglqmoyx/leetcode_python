from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i]:
                index = nums[i] - 1
                value = nums[index]
                nums[index] = 0
                index = value - 1
                while index >=0 and nums[index]:
                    value = nums[index]
                    nums[index] = 0
                    index = value - 1
        for i in range(len(nums)):
            if nums[i] != 0:
                result.append(i + 1)
        return result
