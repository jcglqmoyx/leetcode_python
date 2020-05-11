class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ''
        i = 0
        while i < len(s):
            if s[i] != '#':
                if i >= len(s) - 2 or s[i + 2] != '#':
                    result += chr(ord(s[i]) + 48)
                else:
                    result += chr((ord(s[i]) - 48) * 10 + ord(s[i + 1]) + 48)
                    i += 1
            i += 1
        return result
