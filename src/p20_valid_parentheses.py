class Solution:
    def isValid(self, s: str) -> bool:
        map = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in range(len(s)):
            ch = s[i]
            if map.__contains__(ch):
                if not stack or stack[-1] != map[ch]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)
        return not stack