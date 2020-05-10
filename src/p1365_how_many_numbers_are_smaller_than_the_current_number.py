from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count, ret = [0] * 102, [0] * len(nums)
        for num in nums:
            count[num + 1] += 1
        for i in range(101):
            count[i + 1] += count[i]
        for i in range(len(nums)):
            ret[i] = count[nums[i]]
        return ret