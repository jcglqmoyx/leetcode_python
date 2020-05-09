from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[1][0] - coordinates[0][0] == 0:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
            return True
        slope = self.slope(coordinates, 0, 1)
        for i in range(2, len(coordinates)):
            if self.slope(coordinates, 0, i) != slope:
                return False
        return True

    def slope(self, coordinates: List[List[int]], i: int, j: int) -> float:
        return (coordinates[j][1] - coordinates[i][1]) / (coordinates[j][0] - coordinates[i][0])
