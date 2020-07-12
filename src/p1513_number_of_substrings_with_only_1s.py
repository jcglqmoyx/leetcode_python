class Solution:
    def numSub(self, s: str) -> int:
        result = count = 0
        for c in s:
            if c == '1':
                count += 1
            else:
                result += (count + 1) * count // 2
                count = 0
        result += (count + 1) * count // 2
        return result % 1000000007
