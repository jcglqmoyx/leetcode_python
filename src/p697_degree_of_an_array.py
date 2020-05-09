import collections
from typing import List


# class Solution:
#     def findShortestSubArray(self, nums: List[int]) -> int:
#         max_num = max(nums)
#         counts = [0] * (max_num + 1)
#         pos = [0] * (max_num + 1)
#         degree = shortest_subarray_length = 1
#         for i in range(len(nums)):
#             n = nums[i]
#             counts[n] += 1
#             if counts[n] == 1:
#                 pos[n] = i
#             elif counts[n] > 1:
#                 if counts[n] > degree:
#                     degree = counts[n]
#                     shortest_subarray_length = i - pos[n] + 1
#                 elif counts[n] == degree:
#                     shortest_subarray_length = min(shortest_subarray_length, i - pos[n] + 1)
#         return shortest_subarray_length


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        degree = max(freq.values())
        if degree == 1:
            return 1

        res = float('inf')
        candidates = [n for n in freq if freq[n] == degree]
        for candidate in candidates:
            l = nums.index(candidate)
            r = len(nums) - nums[::-1].index(candidate)
            res = min(res, r - l)

        return res
