class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle, minute_angle = hour * 30 + minutes / 2, minutes * 6
        diff = hour_angle - minute_angle
        if diff < 0:
            diff = -diff
        if diff > 180:
            diff = 360 - diff
        return diff
