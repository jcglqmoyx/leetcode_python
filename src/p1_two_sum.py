from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map:
                return [i, map[diff]]
            map[nums[i]] = i
        return None


nums = [1, 4, 5, 7, 10]
target = 15
print(Solution().twoSum(nums, target))
