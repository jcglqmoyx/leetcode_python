from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []
        arr.sort()
        mid_diff = 2000000
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < mid_diff:
                mid_diff = diff
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == mid_diff:
                result.append([arr[i], arr[i + 1]])
        return result
