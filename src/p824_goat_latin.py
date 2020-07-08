class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')
        result = ''
        for i in range(len(words)):
            word = words[i]
            first = word[0]
            if self.is_vowel(first):
                result += word
            else:
                result += word[1:]
                result += word[0]
            result += 'ma'
            for j in range(i + 1):
                result += 'a'
            if i != len(words) - 1:
                result += ' '
        return result

    def is_vowel(self, c: str) -> bool:
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'
