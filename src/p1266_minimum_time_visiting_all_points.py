from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        step = 0
        for i in range(0, len(points) - 1):
            horizontal_diff, vertical_diff = abs(points[i + 1][1] - points[i][1]), abs(points[i + 1][0] - points[i][0])
            step += max(horizontal_diff, vertical_diff)
        return step


print(Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
print(Solution().minTimeToVisitAllPoints([[3, 2], [-2, 2]]))
