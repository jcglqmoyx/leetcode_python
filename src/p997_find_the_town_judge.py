from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
            return -1
        count = {}
        for pair in trust:
            if pair[1] in count:
                count[pair[1]] += 1
            else:
                count[pair[1]] = 1
        if not count:
            return 1
        max_trust = max(count.values())
        if max_trust != N - 1:
            return -1
        for key in count.keys():
            if count[key] == max_trust:
                town_judge = key
                break
        for pair in trust:
            if pair[0] == town_judge:
                return -1
        return town_judge
