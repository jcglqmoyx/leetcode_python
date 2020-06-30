from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = 0
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        for i in range(n):
            cost += costs[i][0] + costs[i + n][1]
        return cost
