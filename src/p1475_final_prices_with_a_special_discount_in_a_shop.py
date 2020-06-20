from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices)):
            flag = True
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    result.append(prices[i] - prices[j])
                    flag = False
                    break
            if flag:
                result.append(prices[i])
        return result
