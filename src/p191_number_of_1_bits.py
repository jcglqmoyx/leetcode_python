import sys


class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        for i in range(0, 32):
            if (n & 1) == 1:
                ret += 1
            n >>= 1
        return ret


print(Solution().hammingWeight(-3))
print(Solution().hammingWeight(sys.maxsize))
print(Solution().hammingWeight(13))
