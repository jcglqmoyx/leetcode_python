from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string = [0] * len(s)
        for i in range(len(s)):
            string[indices[i]] = s[i]
        return ''.join(string)
