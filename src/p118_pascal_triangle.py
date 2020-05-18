from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[1]]
        if numRows == 1:
            return result
        prev_row = result[len(result) - 1]
        for i in range(2, numRows + 1):
            cur_row = [1]
            for j in range(1, i - 1):
                cur_row.append(prev_row[j - 1] + prev_row[j])
            cur_row.append(1)
            result.append(cur_row)
            prev_row = cur_row
        return result
