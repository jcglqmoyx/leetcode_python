class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ''
        while n:
            n -= 1
            result += (chr(ord('A') + n % 26))
            n //= 26
        return result[::-1]
