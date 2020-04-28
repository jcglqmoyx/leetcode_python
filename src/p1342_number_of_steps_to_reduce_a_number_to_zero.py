class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num:
            if (num & 1) == 0:
                num >>= 1
            else:
                num -= 1
            step += 1
        return step


print(Solution().numberOfSteps(14))
print(Solution().numberOfSteps(8))
print(Solution().numberOfSteps(123))
