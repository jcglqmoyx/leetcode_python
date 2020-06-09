class Solution:
    def isHappy(self, n: int) -> bool:
        fast, slow = self.next(self.next(n)), self.next(n)
        while fast != slow and fast != 1:
            fast = self.next(self.next(fast))
            slow = self.next(slow)
        return fast == 1

    def next(self, n: int) -> int:
        result = 0
        while n:
            last_digit = n % 10
            result += last_digit * last_digit
            n //= 10
        return result
