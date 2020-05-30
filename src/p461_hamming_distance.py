class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x == y:
            return 0
        distance = 1
        flag = 0
        for i in range(32):
            if x % 2 != y % 2:
                if flag == 0:
                    flag = 1
                else:
                    return distance
            else:
                if flag == 1 and x != y:
                    distance += 1
            x >>= 1
            y >>= 1
        return distance
