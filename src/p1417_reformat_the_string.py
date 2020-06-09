class Solution:
    def reformat(self, s: str) -> str:
        count_digit = count_letter = 0
        for c in s:
            if c.isdigit():
                count_digit += 1
            else:
                count_letter += 1
        if abs(count_digit - count_letter) <= 1:
            result = ''
            digit_index = letter_index = 0
            while digit_index < len(s) or letter_index < len(s):
                while digit_index < len(s) and s[digit_index].isalpha():
                    digit_index += 1
                while letter_index < len(s) and s[letter_index].isdigit():
                    letter_index += 1
                if count_digit > count_letter:
                    if digit_index < len(s):
                        result += s[digit_index]
                    if letter_index < len(s):
                        result += s[letter_index]
                else:
                    if letter_index < len(s):
                        result += s[letter_index]
                    if digit_index < len(s):
                        result += s[digit_index]
                digit_index += 1
                letter_index += 1
            return result
        else:
            return ''
