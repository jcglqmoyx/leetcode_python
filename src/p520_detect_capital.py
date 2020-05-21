class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        flag = True
        if ord(word[0]) >= 97:
            for i in range(1, len(word)):
                if ord(word[i]) < 97:
                    flag = False
                    break
            return flag
        if len(word) > 1:
            if ord(word[1]) <= 90:
                for i in range(1, len(word)):
                    if ord(word[i]) > 90:
                        flag = False
                        break
            else:
                for i in range(1, len(word)):
                    if ord(word[i]) < 97:
                        flag = False
                        break
        return flag
