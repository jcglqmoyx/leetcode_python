from typing import List


# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         sum = 0
#         for i in range(len(nums)):
#             sum += nums[i]
#             nums[i] = sum
#         return nums


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
