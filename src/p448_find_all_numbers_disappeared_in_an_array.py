from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappeared_numbers = []
        for i in range(len(nums)):
            if nums[i] <= len(nums):
                j = i
                while j <= len(nums) and nums[j] <= len(nums):
                    cache = nums[nums[j] - 1]
                    nums[nums[j] - 1] += len(nums)
                    j = cachecache
        for i in range(len(nums)):
            if nums[i] <= len(nums):
                disappeared_numbers.append(i + 1)
        return disappeared_numbers


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
