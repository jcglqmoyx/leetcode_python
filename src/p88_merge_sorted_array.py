from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, a, b = m + n - 1, m - 1, n - 1
        while a >= 0 or b >= 0:
            if a >= 0 and b >= 0:
                if nums1[a] < nums2[b]:
                    nums1[i] = nums2[b]
                    b -= 1
                else:
                    nums1[i] = nums1[a]
                    a -= 1
            elif a >= 0:
                nums1[i] = nums1[a]
                a -= 1
            else:
                nums1[i] = nums2[b]
                b -= 1
            i -= 1