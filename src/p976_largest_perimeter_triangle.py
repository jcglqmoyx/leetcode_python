from typing import List


# class Solution:
#     def largestPerimeter(self, A: List[int]) -> int:
#         A.sort()
#         for i in range(len(A) - 1, 1, -1):
#             if A[i] < A[i - 1] + A[i - 2]:
#                 return A[i] + A[i - 1] + A[i - 2]
#         return 0;


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        self.select(A, len(A) - 1)
        self.select(A, len(A) - 2)
        self.select(A, len(A) - 3)
        for i in range(len(A) - 1, 1, -1):
            if A[i] < A[i - 1] + A[i - 2]:
                return A[i] + A[i - 1] + A[i - 2]
            elif i > 2:
                self.select(A, i - 3)
        return 0

    def select(self, arr: List[int], max_index: int) -> None:
        max_value = index = 0
        for i in range(max_index + 1):
            if arr[i] > max_value:
                max_value = arr[i]
                index = i
        temp = arr[index]
        arr[index] = arr[max_index]
        arr[max_index] = temp
