from typing import List


class Solution:
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                     101]

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        product = self.get_product(licensePlate)
        min_length = 1000
        result = ''
        for word in words:
            p = self.get_product(word)
            if p == product or p % product == 0:
                if len(word) < min_length:
                    min_length = len(word)
                    result = word
        return result

    def get_product(self, word: str) -> int:
        product = 1
        for c in word.lower():
            if 97 <= ord(c) <= 122:
                product *= self.prime_numbers[ord(c) - 97]
        return product
