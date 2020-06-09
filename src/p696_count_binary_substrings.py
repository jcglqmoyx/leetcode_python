class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                count += 1
                m, n = i - 1, i + 2
                while m >= 0 and n < len(s) and s[m] == s[i] and s[n] == s[i + 1]:
                    count += 1
                    m -= 1
                    n += 1
        return count
