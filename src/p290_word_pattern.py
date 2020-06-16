class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        m, n = {}, {}
        for i in range(len(pattern)):
            if pattern[i] not in m:
                m[pattern[i]] = words[i]
            else:
                if m[pattern[i]] != words[i]:
                    return False
            if words[i] not in n:
                n[words[i]] = pattern[i]
            else:
                if n[words[i]] != pattern[i]:
                    return False
        return True
