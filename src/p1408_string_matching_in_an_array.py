from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and self.is_substring(words[i], words[j]):
                    result.append(words[i])
        return list(set(result))

    def is_substring(self, a: str, b: str) -> bool:
        if len(a) > len(b):
            return False
        for i in range(len(b) - len(a) + 1):
            if a == b[i:i + len(a)]:
                print(a, b[i:i + len(a)])
                return True
        return False
