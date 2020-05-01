from typing import List, Dict


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length = 0
        map = {}
        for c in chars:
            map[c] = chars.count(c)
        for word in words:
            if self.form_string(word, map):
                length += len(word)
        return length

    def form_string(self, word: str, map: Dict[str, int]) -> bool:
        count = {}
        for ch in word:
            if word.count(ch) > map[ch]:
                return False
        return True