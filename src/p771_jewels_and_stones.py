# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         map = {}
#         for ch in J:
#             map[ch] = 1
#         count = 0
#         for ch in S:
#             if map.__contains__(ch):
#                 count += 1
#         return count

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for ch in S:
            if ch in J:
                count += 1
        return count