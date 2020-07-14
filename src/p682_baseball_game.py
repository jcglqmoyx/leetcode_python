from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = point = 0
        l = []
        for op in ops:
            if op == '+':
                point = l[-1] + l[-2]
                points += point
                l.append(point)
            elif op == 'D':
                point = l[-1] * 2
                points += point
                l.append(point)
            elif op == 'C':
                points -= l[-1]
                del l[-1]
            else:
                point = int(op)
                points += point
                l.append(point)
        return points
