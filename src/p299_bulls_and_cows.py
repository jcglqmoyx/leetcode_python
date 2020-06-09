class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = cow = 0
        cs, cg = [0] * 10, [0] * 10
        for i in range(len(secret)):
            s, g = secret[i], guess[i]
            if s == g:
                bull += 1
            cs[ord(s) - 48] += 1
            cg[ord(g) - 48] += 1
        for i in range(10):
            cow += min(cs[i], cg[i])
        cow -= bull
        return str(bull) + 'A' + str(cow) + 'B'
