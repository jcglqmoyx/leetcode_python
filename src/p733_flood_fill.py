from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.dfs(image, sr, sc, image[sr][sc], newColor)
        return image

    def dfs(self, image: List[List[int]], sr: int, sc: int, originalColor: int, newColor: int) -> None:
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != originalColor or image[sr][sc] == newColor:
            return
        image[sr][sc] = newColor
        self.dfs(image, sr - 1, sc, originalColor, newColor)
        self.dfs(image, sr + 1, sc, originalColor, newColor)
        self.dfs(image, sr, sc - 1, originalColor, newColor)
        self.dfs(image, sr, sc + 1, originalColor, newColor)
