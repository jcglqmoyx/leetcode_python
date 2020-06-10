class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        i = j = 0
        while i < len(s):
            while s[i] != t[j]:
                j += 1
                if j == len(t):
                    return False
            i += 1
            j += 1
            if j == len(t) and i < len(s):
                return False
        return True
