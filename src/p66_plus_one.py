from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = digits[-1] + 1
        carry = sum // 10
        digits[-1] = sum % 10
        for i in range(len(digits) - 2, -1, -1):
            sum = digits[i] + carry
            digits[i] = sum % 10
            if sum < 10:
                return digits
            carry = sum // 10
        if carry:
            digits.insert(0, 1)
        return digits
