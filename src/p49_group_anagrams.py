from typing import List


class Solution:
    prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groups = {}
        for word in strs:
            index = self.index(word)
            if index in groups.keys():
                anagrams = groups[index]
                anagrams.append(word)
            else:
                groups[index] = [word]
        for anagram in groups.values():
            result.append(anagram)
        return result

    def index(self, word: str) -> int:
        index = 1
        for c in word:
            index *= self.prime_nums[ord(c) - 97]
        return index
