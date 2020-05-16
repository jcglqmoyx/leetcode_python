# from typing import List
#
#
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         for i in range(len(nums)):
#             num = nums[i]
#             two_sum = self.two_sum(nums, i)
#             if two_sum:
#                 two_sum.append(num)
#                 result.append(two_sum)
#         return result
#
#     def two_sum(self, nums: List[int], i: int) -> List[int]:
#         for j in range(len(nums)):
#             if j != i:
#
