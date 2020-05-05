from typing import List
from sys import maxsize


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = -maxsize
        for num in nums:
            if num > third:
                if num > second:
                    if num > first:
                        third = second
                        second = first
                        first = num
                    elif num < first:
                        third = second
                        second = num
                elif num < second:
                    third = num
        return third if third != -maxsize else first
