from typing import List


# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         result = []
#         max = 0
#         for candy in candies:
#             if candy > max:
#                 max = candy
#         for candy in candies:
#             if candy + extraCandies >= max:
#                 result.append(True)
#             else:
#                 result.append(False)
#         return result


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        _max = max(candies)
        for candy in candies:
            if candy + extraCandies >= max:
                result.append(True)
            else:
                result.append(False)
        return result
