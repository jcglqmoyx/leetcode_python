from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        result = []
        start, count = 0, 1
        for i in range(len(S) - 1):
            if S[i] == S[i + 1]:
                count += 1
            else:
                if count >= 3:
                    positions = [start, i]
                    result.append(positions)
                start = i + 1
                count = 1
            if i == len(S) - 2:
                if count >= 3:
                    positions = [start, i + 1]
                    result.append(positions)
        return result
