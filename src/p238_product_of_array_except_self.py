from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, result = [0] * len(nums), [1] * len(nums), [0] * len(nums)
        left[0] = 1
        right[-1] = 1
        for i in range(1, len(left)):
            left[i] = left[i - 1] * nums[i - 1]
            right[len(right) - i - 1] = right[len(right) - i] * nums[len(nums) - i]
        for i in range(len(result)):
            result[i] = left[i] * right[i]
        return result
