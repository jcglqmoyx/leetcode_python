from typing import List


# class Solution:
#     def findLucky(self, arr: List[int]) -> int:
#         freq = [0] * 501
#         for num in arr:
#             freq[num] += 1
#         for i in range(500, 0, -1):
#             if freq[i] == i:
#                 return i
#         return -1


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        result = []
        for key in freq.keys():
            if freq[key] == key:
                result.append(key)
        if not result:
            return -1
        else:
            return max(result)
