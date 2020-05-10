from typing import List


# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         if k < 0:
#             return 0
#         count = 0
#         if k == 0:
#             for num in nums:
#                 if nums.count(num) > 1:
#                     while num in nums:
#                         nums.remove(num)
#                     count += 1
#             return count
#         nums = list(set(nums))
#         for num in nums:
#             if num + k in nums:
#                 count += 1
#         return count


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        cnt = []
        if k < 0:
            return 0
        if k == 0:
            for num in nums:
                if nums.count(num) > 1:
                    cnt.append((num, num + k))
            return len(set(cnt))
        nums = set(nums)
        for num in nums:
            if num + k in nums:
                pairs += 1
        return pairs
