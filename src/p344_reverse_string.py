from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # for i in range(0, len(s) // 2):
        #     high = len(s) - 1 - i
        #     temp = s[i]
        #     s[i] = s[high]
        #     s[high] = temp

        return s.reverse()