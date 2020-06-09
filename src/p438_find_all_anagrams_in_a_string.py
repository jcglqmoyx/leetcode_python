from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if not s or not p or len(s) < len(p):
            return result
        count_p, count_s = [0] * 26, [0] * 26
        for i in range(len(p)):
            count_p[ord(p[i]) - 97] += 1
            count_s[ord(s[i]) - 97] += 1
        flag = True
        for i in range(26):
            if count_p[i] != count_s[i]:
                flag = False
                break
        if flag:
            result.append(0)
        for i in range(1, len(s) - len(p) + 1):
            count_s[ord(s[i - 1]) - 97] -= 1
            count_s[ord(s[i + len(p) - 1]) - 97] += 1
            flag = True
            for index in range(26):
                if count_p[index] != count_s[index]:
                    flag = False
                    break
            if flag:
                result.append(i)
        return result
