from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[flag]:
                flag += 1
                nums[flag] = nums[i]
        for i in range(flag + 1, len(nums)):
            nums[i] = 0
        return flag + 1


print(Solution().removeDuplicates([1, 1, 2]))
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))