from typing import List


# class Solution:
#     def distributeCandies(self, candies: List[int]) -> int:
#         result = 0
#         kinds = [0] * 200001
#         for candy in candies:
#             kinds[candy + 100000] += 1
#         for n in kinds:
#             if n:
#                 result += 1
#                 if result >= len(candies) // 2:
#                     return len(candies) // 2
#         return result


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        result = 0
        kinds = {}
        for candy in candies:
            kinds[candy] = 1
        if len(kinds) >= len(candies) // 2:
            return len(candies) // 2
        else:
            return len(kinds)
