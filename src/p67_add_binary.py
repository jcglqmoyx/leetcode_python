class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry = len(a) - 1, len(b) - 1, 0
        result = ''
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                sum = ord(a[i]) + ord(b[j]) - 96 + carry
                i -= 1
                j -= 1
            elif i >= 0:
                sum = ord(a[i]) - 48 + carry
                i -= 1
            else:
                sum = ord(b[j]) - 48 + carry
                j -= 1
            carry = sum // 2
            result += str(sum % 2)
        if carry:
            result += '1'
        return result[::-1]
