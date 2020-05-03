from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        map = {}
        for strs in paths:
            map[strs[0]] = strs[1]

        for strs in paths:
            if strs[1] not in map:
                return strs[1]
        return None
