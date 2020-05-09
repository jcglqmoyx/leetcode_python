from _ast import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        low, high = 0, len(A) - 1
        while low < high:
            mid = low + (high - low) // 2
            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] < A[mid - 1]:
                high = mid
            else:
                low = mid + 1
        return low
