class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs, ct = [0] * 123, [0] * 123
        for c in s:
            cs[ord(c)] += 1
        for c in t:
            ct[ord(c)] += 1
        for i in range(97, 123):
            if cs[i] != ct[i]:
                return chr(i)
        return 'a'
