class Solution:
    def maxPower(self, s: str) -> int:
        power = max_power = 1
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                power += 1
            else:
                if power > max_power:
                    max_power = power
                power = 1
        if power > max_power:
            max_power = power
        return max_power