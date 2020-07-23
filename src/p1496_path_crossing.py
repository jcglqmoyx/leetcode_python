class Solution:
    def isPathCrossing(self, path: str) -> bool:
        positions = set()
        x = y = 0
        positions.add('0 0')
        for direction in path:
            if direction == 'W':
                x -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'N':
                y += 1
            else:
                y -= 1
            position = str(x) + ' ' + str(y)
            if position in positions:
                return True
            positions.add(position)

        return False
