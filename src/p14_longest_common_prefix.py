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