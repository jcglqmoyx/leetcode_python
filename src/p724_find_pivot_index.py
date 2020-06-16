from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        left, right = [0] * len(nums), [0] * len(nums)
        left_sum, right_sum = nums[0], nums[-1]
        left[0] = right[len(right) - 1] = 0
        for i in range(1, len(nums)):
            left[i] = left_sum
            left_sum += nums[i]
        for i in range(len(right) - 2, -1, -1):
            right[i] = right_sum
            right_sum += nums[i]
        for i in range(len(nums)):
            if left[i] == right[i]:
                return i
        return -1
