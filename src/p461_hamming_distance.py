class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        for i in range(32):
            if x % 2 != y % 2:
                distance += 1
            x >>= 1
            y >>= 1
        return distance
