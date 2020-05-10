from typing import List


# class Solution:
#     def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
#         for i in range(len(A)):
#             nums = A[i]
#             for j in range(len(nums) // 2):
#                 temp = nums[j]
#                 nums[j] = nums[len(nums) - 1 - j]
#                 nums[len(nums) - 1 - j] = temp
#             for j in range(len(nums)):
#                 nums[j] ^= 1
#         return A


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for nums in A:
            nums = nums[::-1]
            for i in range(len(nums)):
                nums[i] ^= 1
            result.append(nums)
        return result
