class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - 97] += 1
            counts[ord(t[i]) - 97] -= 1
        for count in counts:
            if count > 0:
                steps += count
                print(count)
        return steps
