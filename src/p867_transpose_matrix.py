from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(A[0])):
            row = []
            for j in range(len(A)):
                row.append(A[j][i])
            result.append(row)
        return result
