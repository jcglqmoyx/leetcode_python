from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = maxArea = 0
        low, high = 0, len(height) - 1
        while low < high:
            area = (high - low) * min(height[low], height[high])
            maxArea = max(area, maxArea)
            if height[low] < height[high]:
                low += 1
            elif height[high] < height[low]:
                high -= 1
            else:
                low += 1
                high -= 1
        return maxArea
