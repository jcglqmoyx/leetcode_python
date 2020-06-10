from typing import List


# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         intersection = []
#         for num in nums2:
#             if num in nums1 and num not in intersection:
#                 intersection.append(num)
#         return intersection

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
