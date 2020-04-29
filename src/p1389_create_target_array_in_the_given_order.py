from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            ret.insert(index[i], nums[i])
        return ret


print(Solution().createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
print(Solution().createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))
print(Solution().createTargetArray([1], [0]))
