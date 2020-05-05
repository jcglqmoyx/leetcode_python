from typing import List


# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         nums.sort()
#         sum = 0
#         for i in range(0, len(nums), 2):
#             sum += nums[i]
#         return sum

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        counts = [0] * 20001
        for num in nums:
            counts[num + 10000] += 1
        flag = 1
        sum = 0
        for i in range(len(counts)):
            if counts[i]:
                while counts[i]:
                    if flag:
                        sum += i - 10000
                        flag = 0
                    else:
                        flag = 1
                    counts[i] -= 1
        return sum
