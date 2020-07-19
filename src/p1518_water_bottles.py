class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        number = numBottles
        while numBottles >= numExchange:
            temp = numBottles // numExchange
            number += temp
            numBottles = numBottles - temp * numExchange + temp
        return number
