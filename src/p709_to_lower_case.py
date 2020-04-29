class Solution:
    def toLowerCase(self, str: str) -> str:
        ret = ''
        for c in str:
            value = ord(c)
            if 65 <= value <= 90:
                ret += chr(value + 32)
            else:
                ret += c
        return ret


print(Solution().toLowerCase('Hello'))
print(Solution().toLowerCase('here'))
print(Solution().toLowerCase('LOVELY'))
