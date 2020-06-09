from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        low, high = 0, len(S)
        result = []
        for c in S:
            if c == 'D':
                result.append(high)
                high -= 1
            else:
                result.append(low)
                low += 1
        result.append(low)
        return result
