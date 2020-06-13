def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g > 0:
                low = mid + 1
            else:
                high = mid
        return low
