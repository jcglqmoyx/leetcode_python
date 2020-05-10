class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        result = ''
        flag = True if num >= 0 else False
        if num < 0:
            num = -num
        while num:
            last_digit = num % 7
            result += str(last_digit)
            num //= 7
        if not flag:
            result += '-'
        return result[::-1]
