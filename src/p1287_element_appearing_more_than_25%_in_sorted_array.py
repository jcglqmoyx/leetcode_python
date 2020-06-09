from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 1
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                count += 1
            else:
                count = 1
            if count > len(arr) / 4:
                return arr[i]
        return count
