from typing import List


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(M[0]) for i in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                result[i][j] = self.average(M, i, j)
        return result

    def average(self, M: List[List[int]], i: int, j: int) -> int:
        if i > 0:
            if j > 0:
                if i < len(M):
                    if j < len(M[0]):
                        return (M[i - 1][j - 1] + M[i - 1][j] + M[i][j - 1] + M[i][j] + M[i + 1][j - 1] + M[i + 1][j] +
                                M[i - 1][j + 1] + M[i][j + 1] + M[i + 1][j + 1]) // 9
                    else:
                        return (M[i - 1][j - 1] + M[i - 1][j] + M[i][j - 1] + M[i][j] + M[i + 1][j - 1] + M[i + 1][
                            j]) // 6
                else:
                    if j < len(M[0]):
                        return (M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][j + 1] + M[i][j -] + M[i][j] + M[i][
                            j + 1]) // 6
                    else:
                        return (M[i - 1][j - 1] + M[i - 1][j] + M[i][j - 1] + M[i][j]) // 4
            else:
                if i < len(M):
                    return (M[i - 1][j] + M[i - 1][j + 1] + M[i][j] + M[i][j + 1] + M[i + 1][j] + M[i + 1][j + 1]) // 6
                else:
                    return (M[i][j] + M[i][j + 1] + M[i - 1][j] + M[i - 1][j + 1]) // 4
        else:
            if j > 0:
                if j < len(M[0]):
                    return (M[i][j - 1] + M[i][j] + M[i][j + 1] + M[i + 1][j - 1] + M[i + 1][j] + M[i + 1][j + 1]) // 6
                else:

