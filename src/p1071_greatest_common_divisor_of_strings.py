class Solution:
    def frequencySort(self, s: str) -> str:
        counts = [0] * 128
        for c in s:
            counts[ord(c)] += 1
        result = ''
        for i in range(len(s)):
            index = max = 0
            for j in range(128):
                if max < counts[j]:
                    max = counts[j]
                    index = j
            while counts[index]:
                result += chr(index)
                counts[index] -= 1
        return result
