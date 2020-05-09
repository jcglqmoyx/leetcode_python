class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return "11"
        last = self.countAndSay(n - 1)
        count = i = 0
        result = ''
        while i < len(last) - 1:
            count += 1
            if last[i] != last[i + 1]:
                result += str(count) + last[i]
                count = 0
            i += 1
        if last[-2] != last[-1]:
            result += '1'
        else:
            result += str(count + 1)
        result += last[-1]
        return result
