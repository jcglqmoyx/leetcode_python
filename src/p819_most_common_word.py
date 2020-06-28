from typing import List

"""
the algorithm remains to be improved
"""
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = {}
        paragraph = paragraph.lower()
        start = 0
        for end in range(len(paragraph)):
            if not paragraph[end].isalpha():
                word = paragraph[start:end]
                start = end + 1
                if word != '':
                    if word in count:
                        count[word] += 1
                    else:
                        count[word] = 1
            if end == len(paragraph) - 1:
                word = paragraph[start:]
                if word != '':
                    if word in count:
                        count[word] += 1
                    else:
                        count[word] = 1
        values = count.values()
        for value in sorted(values, reverse=True):
            for key in count:
                if count[key] == value and key not in banned:
                    return key
        return ''
