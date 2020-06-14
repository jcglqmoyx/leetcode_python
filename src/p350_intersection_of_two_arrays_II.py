from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1, map2 = {}, {}
        for num in nums1:
            if num not in map1:
                map1[num] = 1
            else:
                map1[num] += 1
        for num in nums2:
            if num not in map2:
                map2[num] = 1
            else:
                map2[num] += 1
        result = []
        for num in map1:
            if num in map2:
                number = min(map1[num], map2[num])
                for i in range(number):
                    result.append(num)
        return result
