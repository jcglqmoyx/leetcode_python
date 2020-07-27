from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        maximum = sum
        for i in range(1, len(nums) - k + 1):
            sum = sum - nums[i - 1] + nums[i + k - 1]
            maximum = max(maximum, sum)
        return maximum / k
