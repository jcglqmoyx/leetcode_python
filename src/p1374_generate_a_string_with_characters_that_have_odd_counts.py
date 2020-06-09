class Solution:
    def generateTheString(self, n: int) -> str:
        result = ''
        if n % 2:
            for i in range(n):
                result += 'a'
        else:
            for i in range(n - 1):
                result += 'a'
            result += 'b'
        return result
