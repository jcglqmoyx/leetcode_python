from typing import List


class Solution:
    d = {'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'y': 0, 'u': 0, 'i': 0, 'o': 0, 'p': 0,
         'a': 1, 's': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l': 1,
         'z': 2, 'x': 2, 'c': 2, 'v': 2, 'b': 2, 'n': 2, 'm': 2}

    def findWords(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            if self.characters_in_one_row(word):
                result.append(word)
        return result

    def characters_in_one_row(self, word: str) -> bool:
        word = word.lower()

        for i in range(0, len(word) - 1):
            if self.d[word[i]] != self.d[word[i + 1]]:
                return False
        return True
