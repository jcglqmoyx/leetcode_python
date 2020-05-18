# class Solution:
#     def dayOfYear(self, date: str) -> int:
#         month = (ord(date[5]) - 48) * 10 + ord(date[6]) - 48
#         day = (ord(date[8]) - 48) * 10 + ord(date[9]) - 48
#         result = 0
#         if month == 1:
#             return day
#         result += 31
#         if month == 2:
#             result += day
#             return result
#         if self.is_leap_year(date[:4]):
#             result += 29
#         else:
#             result += 28
#         if month == 3:
#             result += day
#             return result
#         result += 31
#         if month == 4:
#             result += day
#             return result
#         result += 30
#         if month == 5:
#             result += day
#             return result
#         result += 31
#         if month == 6:
#             result += day
#             return result
#         result += 30
#         if month == 7:
#             result += day
#             return result
#         result += 31
#         if month == 8:
#             result += day
#             return result
#         result += 31
#         if month == 9:
#             result += day
#             return result
#         result += 30
#         if month == 10:
#             result += day
#             return result
#         result += 31
#         if month == 11:
#             result += day
#             return result
#         result += 30
#         if month == 12:
#             result += day
#         return result
#
#     def is_leap_year(self, year: str) -> bool:
#         year = (ord(year[0]) - 48) * 1000 + (ord(year[1]) - 48) * 100 + (ord(year[2]) - 48) * 10 + ord(year[3]) - 48
#         return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


class Solution:
    def dayOfYear(self, date: str) -> int:
        l = list(map(int, date.split("-")))

        if l[0] % 4 != 0 or l[0] % 4 == 0 and (l[0] % 100 == 0 and l[0] % 400 != 0):
            m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            t = 0
            i = 1
            while i < l[1]:
                t += m[i - 1]
                i += 1
            return t + l[2]
        else:
            m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            t = 0
            i = 1
            while i < l[1]:
                t += m[i - 1]
                i += 1
            return t + l[2]
