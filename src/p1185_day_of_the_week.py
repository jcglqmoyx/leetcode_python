import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date_time = datetime.datetime(year, month, day)
        values = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return values[date_time.weekday()]
