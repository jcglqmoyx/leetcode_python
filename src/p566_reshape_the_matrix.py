from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
        result, arr = [], []
        size = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                size += 1
                arr.append(nums[i][j])
                if size == c:
                    result.append(arr)
                    size = 0
                    arr = []
        return result
