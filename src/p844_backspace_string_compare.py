class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = t = ''
        for c in S:
            if c == '#':
                if len(s) > 0:
                    s = s[:-1]
            else:
                s += c
        for c in T:
            if c == '#':
                if len(t) > 0:
                    t = t[:-1]
            else:
                t += c
        return s == t
