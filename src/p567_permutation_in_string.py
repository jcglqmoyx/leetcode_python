class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts1, counts2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            counts1[ord(s1[i]) - 97] += 1
            counts2[ord(s2[i]) - 97] += 1
        flag = True
        for i in range(26):
            if counts1[i] != counts2[i]:
                flag = False
                break
        if flag:
            return True
        for i in range(1, len(s2) - len(s1) + 1):
            counts2[ord(s2[i - 1]) - 97] -= 1
            counts2[ord(s2[i + len(s1) - 1]) - 97] += 1
            flag = True
            for j in range(26):
                if counts1[j] != counts2[j]:
                    flag = False
                    break
            if flag:
                return True
