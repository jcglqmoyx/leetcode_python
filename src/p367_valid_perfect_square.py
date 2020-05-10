class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        low, high = 0, num
        while low < high:
            mid = low + (high - low) // 2
            sqr = mid ** 2
            if sqr == num:
                return True
            elif sqr < num:
                low = mid + 1
            else:
                high = mid
        return False
