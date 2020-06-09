import math
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqrt = int(math.sqrt(area))
        while area % sqrt != 0:
            sqrt -= 1
        return [area // sqrt, sqrt]
