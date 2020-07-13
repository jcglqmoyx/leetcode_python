class Solution:
    def maxScore(self, s: str) -> int:
        left, right = [0] * len(s), [0] * len(s)
        left[0] = 0
        right[-1] = 0
        maximum_score = 0
        left_max = right_max = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                left[i + 1] += left_max + 1
                left_max = left[i]
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                right[i]
                right[i - 1] += 1
        for i in range(len(s)):
            maximum_score = max(maximum_score, left[i] + right[i])
        return maximum_score
