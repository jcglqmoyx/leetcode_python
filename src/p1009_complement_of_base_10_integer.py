class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        sum, cp = 0, N
        while N:
            sum = (sum << 1) + 1
            N >>= 1
        return sum ^ cp
