class Solution:
    def sortString(self, s: str) -> str:
        counts = {}
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        result = ''
        n = 0
        while n < len(s):
            for i in range(97, 123):
                if chr(i) in counts:
                    result += chr(i)
                    n += 1
                    counts[chr(i)] -= 1
                    if counts[chr(i)] == 0:
                        del counts[chr(i)]
            for i in range(122, 96, -1):
                if chr(i) in counts:
                    result += chr(i)
                    n += 1
                    counts[chr(i)] -= 1
                    if counts[chr(i)] == 0:
                        del counts[chr(i)]
        return result
