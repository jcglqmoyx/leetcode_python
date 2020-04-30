class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        sum = 0
        for i in range(len(s)):
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                sum -= values[s[i]]
            else:
                sum += values[s[i]]
        return sum