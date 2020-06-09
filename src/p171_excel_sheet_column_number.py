class Solution:
    def titleToNumber(self, s: str) -> int:
        num, length = 0, len(s)
        for i in range(length):
            num += pow(26, length - i - 1) * (ord(s[i]) - 64)
        return num
