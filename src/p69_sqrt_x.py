import sys


class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = low + (high - low) // 2
            sqr = pow(mid, 2)
            if sqr == x or sqr < x and pow(mid + 1, 2) > x:
                return mid
            elif sqr < x:
                low = mid + 1
            else:
                high = mid
        return mid


print(Solution().mySqrt(1))
print(Solution().mySqrt(2))
print(Solution().mySqrt(25))
print(Solution().mySqrt(26))
print(Solution().mySqrt(sys.maxsize))