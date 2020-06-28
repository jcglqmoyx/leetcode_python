from typing import List


# using two arrays can be fasters
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        result = []
        arr1.sort()
        for num in arr1:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for num in arr2:
            for i in range(d[num]):
                result.append(num)
        for num in arr1:
            if num not in arr2:
                result.append(num)
        return result
