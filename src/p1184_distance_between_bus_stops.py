from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            return self.distanceBetweenBusStops(distance, destination, start)
        distance1 = distance2 = 0
        for i in range(start, destination):
            distance1 += distance[i]
        for j in range(destination, len(distance)):
            distance2 += distance[j]
        for j in range(0, start):
            distance2 += distance[j]
        return min(distance1, distance2)
