from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length = 0
        for word in words:
            if self.form_string(word, chars):
                length += len(word)
        return length

    def form_string(self, word: str, chars: str) -> bool:
        map = [0] * 123
        for ch in chars:
            map[ord(ch)] += 1
        for ch in word:
            map[ord(ch)] -= 1
            if map[ord(ch)] < 0:
                return False
        return True
