from typing import List, Dict


def form_string(word: str, map: Dict[str, int]) -> bool:
    for ch in word:
        if not ch in map or word.count(ch) > map[ch]:
            return False
    return True


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length = 0
        map = {}
        for c in chars:
            map[c] = chars.count(c)
        for word in words:
            if form_string(word, map):
                length += len(word)
        return length
