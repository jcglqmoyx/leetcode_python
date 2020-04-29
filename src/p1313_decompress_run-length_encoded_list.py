from typing import List


# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         ret = []
#         for index in range(0, len(nums), 2):
#             freq, value = nums[index], nums[index + 1]
#             for i in range(0, freq):
#                 ret.append(nums[index + 1])
#         return ret


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        t = list()
        for i in range(0, len(nums), 2):
            t += [nums[i + 1]] * nums[i]
        return t


print(Solution().decompressRLElist([1, 2, 3, 4]))
print(Solution().decompressRLElist([1, 1, 2, 3]))
