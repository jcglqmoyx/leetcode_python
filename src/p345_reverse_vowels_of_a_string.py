class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = []
        for c in s:
            chars.append(c)
        low, high = 0, len(s) - 1
        while low < high:
            while not self.is_vowel(s[low]) and low < high:
                low += 1
            while not self.is_vowel(s[high]) and low < high:
                high -= 1
            temp = chars[low]
            chars[low] = s[high]
            chars[high] = temp
            low += 1
            high -= 1
        return ''.join(chars)

    def is_vowel(self, c: str) -> bool:
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'
