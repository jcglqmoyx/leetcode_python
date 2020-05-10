from typing import List


# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         result = []
#         for i in range(len(arr)):
#             result.append(max_value_to_right(arr, i))
#         result[-1] = -1
#         return result
#
#     def max_value_to_right(self, arr: List[int], index: int) -> int:
#         max = -maxsize
#         for i in range(index + 1, len(arr)):
#             if arr[i] > max:
#                 max = arr[i]
#         return max


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        _max = -1
        result = [0] * len(arr)
        for i in range(len(arr) - 2, -1, -1):
            _max = max(_max, arr[i + 1])
            result[i] = _max
        result[-1] = -1
        return result
