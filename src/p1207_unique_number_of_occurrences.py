from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for num in arr:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1
        return len(set(count.values())) == len(count)
