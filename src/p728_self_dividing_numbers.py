from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            if self.selfDivisible(num):
                result.append(num)
        return result

    def selfDivisible(self, num: int) -> bool:
        temp = num
        while num:
            last_digit = num % 10
            if last_digit == 0 or temp % last_digit != 0:
                return False
            num //= 10
        return True


print(Solution().selfDividingNumbers(1, 22))
