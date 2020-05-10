from typing import List


# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         count = 0
#         for num in nums:
#             if (1 + int(log10(num)) & 1) == 0:
#                 count += 1
#         return count


# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         count = 0
#         for num in nums:
#             if 9 < num < 100 or 999 < num < 10000:
#                 count += 1
#         return count

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if (len(str(num)) & 1) == 0:
                count += 1
        return count