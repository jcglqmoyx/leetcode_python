# class Solution:
#     def daysBetweenDates(self, date1: str, date2: str) -> int:
#         year1 = ord(date1[0]) * 1000 + ord(date1[1]) * 100 + ord(date1[2]) * 10 + ord(date1[3])
#         year2 = ord(date2[0]) * 1000 + ord(date2[1]) * 100 + ord(date2[2]) * 10 + ord(date2[3])
#         month1 = ord(date1[5]) * 10 + ord(date1[6])
#         month2 = ord(date2[5]) * 10 + ord(date2[6])
#         day1 = ord(date1[8]) * 10 + ord(date1[9])
#         day2 = ord(date2[8]) * 10 + ord(date2[9])
#         result = 0
#
#
#     def is_leap_year(self, year: int) -> bool:
#         return year % 400 == 0 or year % 4 == 0 and year % 100 != 0
