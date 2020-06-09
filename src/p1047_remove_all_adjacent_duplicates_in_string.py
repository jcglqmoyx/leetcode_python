class Solution:
    def removeDuplicates(self, S: str) -> str:
        chars = []
        chars.append(S[0])
        for i in range(1, len(S)):
            if chars and S[i] == chars[-1]:
                chars.pop()
            else:
                chars.append(S[i])
        result = ''
        for char in chars:
            result += char
        return result
