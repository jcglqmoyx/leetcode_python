class Solution:
    def maxScore(self, s: str) -> int:
        zeros, ones = [0] * (len(s) + 1), [0] * (len(s) + 1)
        count_zero = count_one = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                count_zero += 1
                zeros[i + 1] = count_zero
        for i in range(len(s) - 1, 0, -1):
            if s[i] == '1':
                count_one += 1
                ones[i] = count_one
        max_score = 0
        for i in range(1, len(s)):
            max_score = max(zeros[i] + ones[i], max_score)
        return max_score
