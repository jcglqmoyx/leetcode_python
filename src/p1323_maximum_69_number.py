class Solution:
    def maximum69Number(self, num: int) -> int:
        temp, additon, flag = num, 0, 0
        while num:
            last_digit = num % 10
            flag += 1
            if last_digit == 6:
                additon = 3 * int(pow(10, flag - 1))
            num //= 10
        return temp + additon
