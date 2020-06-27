class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        count = [0] * 123
        flag = False
        for c in s:
            count[ord(c)] += 1
        for i in range(65, 123):
            if count[i] % 2 == 0:
                result += count[i]
            else:
                flag = True
                result += count[i] - 1
        return result + 1 if flag else result
