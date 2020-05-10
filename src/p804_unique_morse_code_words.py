from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformations = []
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                 "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                 "-.--", "--.."]
        for word in words:
            transformation = ''
            for c in word:
                transformation += codes[ord(c) - 97]
            transformations.append(transformation)
        return len(set(transformations))
