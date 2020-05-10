class Solution:
    def findComplement(self, num: int) -> int:
        cp, sum = num, 0
        while num:
            sum = (sum << 1) + 1
            num >>= 1
        return sum ^ cp
