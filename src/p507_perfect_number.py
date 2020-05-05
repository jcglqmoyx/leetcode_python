import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sum = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if not num % i:
                sum += i
                if i != num // i:
                    sum += num // i
        return sum == num
