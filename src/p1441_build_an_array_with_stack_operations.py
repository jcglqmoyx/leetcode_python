from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        i, j = 0, 1
        while j <= n:
            if target[i] == j:
                result.append('Push')
                i += 1
                j += 1
            else:
                while target[i] != j:
                    result.append('Push')
                    result.append('Pop')
                    j += 1
            if i == len(target):
                break
        return result
