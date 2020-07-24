from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        result = []
        for i in range(len(words)):
            words[i] = self.freq(words[i])
        words.sort()
        for i in range(len(queries)):
            freq = self.freq(queries[i])
            low, high = 0, len(words) - 1
            while low < high:
                mid = low + (high - low) // 2
                if words[mid] == freq:
                    result[i] = len(words) - freq
                    break
                elif words[mid] < freq:
                    low = mid + 1
                else:
                    high = mid
            result[i] = len(words) - low
        return result

    def freq(self, word: str) -> int:
        d = {}
        for c in word:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for i in range(97, 123):
            if str(chr(i)) in d and d[str(chr(i))] != 0:
                return d[str(chr(i))]
        return 0
