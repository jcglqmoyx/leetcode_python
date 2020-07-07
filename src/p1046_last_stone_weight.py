from typing import List


# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         while len(stones) > 1:
#             stones.sort()
#             stones[-1] -= stones[-2]
#             if stones[-1] == 0:
#                 del stones[-1]
#                 del stones[-1]
#             else:
#                 del stones[-2]
#         if len(stones) == 1:
#             return stones[0]
#         else:
#             return 0

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        while True:
            indices = self.get_heaviest_stones(stones)
            x, y = indices[0], indices[1]
            if stones[x] > 0 and stones[y] > 0:
                if stones[x] == stones[y]:
                    stones[x] = 0
                    stones[y] = 0
                else:
                    stones[x] -= stones[y]
                    stones[y] = 0
            else:
                return stones[x]

    def get_heaviest_stones(self, stones: List[int]) -> List[int]:
        x = y = 0
        first = second = -1
        for i in range(len(stones)):
            if stones[i] > second:
                if stones[i] > first:
                    second = first
                    first = stones[i]
                    y = x
                    x = i
                else:
                    second = stones[i]
                    y = i
        return [x, y]
