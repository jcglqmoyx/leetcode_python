class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        i = 0
        while i + len(needle) <= len(haystack):
            if haystack[i:i + len(needle)] == needle:
                return i
            i += 1
        return -1
