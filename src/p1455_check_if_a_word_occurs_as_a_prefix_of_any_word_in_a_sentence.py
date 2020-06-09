class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        index = 1
        for i in range(0, len(sentence) - len(searchWord) + 1):
            if sentence[i] == ' ':
                index += 1
            if (i == 0 or sentence[i - 1] == ' ') and sentence[i:i + len(searchWord)] == searchWord:
                return index
        return -1
