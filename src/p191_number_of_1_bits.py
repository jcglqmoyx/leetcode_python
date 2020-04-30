import sys


class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        for i in range(0, 32):
            if (n & 1) == 1:
                ret += 1
            n >>= 1
        return ret