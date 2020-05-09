class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if k:
                    return k
            else:
                k += 1
        return k
