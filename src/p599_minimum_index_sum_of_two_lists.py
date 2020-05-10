from sys import maxsize
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = {}
        for i in range(len(list1)):
            map1[list1[i]] = i
        min_index_sum = maxsize
        result = []
        for i in range(len(list2)):
            if list2[i] in map1:
                current_sum = map1[list2[i]] + i
                if current_sum < min_index_sum:
                    result.clear()
                    min_index_sum = current_sum
                    result.append(list2[i])
                elif current_sum == min_index_sum:
                    result.append(list2[i])
        return result
