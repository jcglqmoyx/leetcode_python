class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            sqr1, sqr2 = mid * (mid + 1) // 2, (mid + 1) * (mid + 2) // 2
            if sqr1 <= n < sqr2:
                return mid
            elif sqr1 > n:
                high = mid
            else:
                low = mid + 1
        return low
