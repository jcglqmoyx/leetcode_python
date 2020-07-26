class Solution:
    def numSplits(self, s: str) -> int:
        left, right = set(), set()
        left_count, right_count = [0] * (len(s) + 1), [0] * (len(s) + 1)
        for i in range(len(s) - 1):
            left.add(s[i])
            left_count[i + 1] = len(left)
            right.add(s[len(s) - 1 - i])
            right_count[len(s) - 1 - i] = len(right)
        result = 0
        for i in range(1, len(s)):
            if left_count[i] == right_count[i]:
                result += 1
        return result
