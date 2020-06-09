from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = {}
        for i in range(len(target)):
            if target[i] in count:
                count[target[i]] += 1
            else:
                count[target[i]] = 1
            if arr[i] in count:
                count[arr[i]] -= 1
            else:
                count[arr[i]] = -1
        for key in count:
            if count[key] != 0:
                return False
        return True
