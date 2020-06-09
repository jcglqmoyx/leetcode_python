from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        result = []
        sum = sub_sum = 0
        for num in nums:
            sum += num
        nums.sort(reverse=True)
        for i in range(len(nums)):
            sub_sum += nums[i]
            result.append(nums[i])
            if sub_sum > sum / 2:
                break
        return result
