class Solution:
    def countPrimes(self, n: int) -> int:
        flags = [False] * n
        count = 0
        for i in range(2, n):
            if not flags[i]:
                count += 1
                for j in range(i * 2, n, i):
                    flags[j] = True
        return count
