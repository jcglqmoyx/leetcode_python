from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""
        i = 0
        while i < len(strs[0]):
            c = strs[0][i]
            for str in strs:
                if i == len(str) or str[i] != c:
                    return str[:i]
            i += 1
        return strs[0][:i]


strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
strs3 = None
strs4 = []
strs5 = [""]
strs6 = ["abb", "abc"]
print(Solution().longestCommonPrefix(strs1))
print(Solution().longestCommonPrefix(strs2))
print(Solution().longestCommonPrefix(strs3))
print(Solution().longestCommonPrefix(strs4))
print(Solution().longestCommonPrefix(strs5))
print(Solution().longestCommonPrefix(strs6))