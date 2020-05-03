def isBadVersion(version):
    pass


# class Solution:
#     def firstBadVersion(self, n):
#         low, high = 1, n
#
#         while low < high:
#             mid = low + (high - low) / 2
#             if not isBadVersion(mid) and isBadVersion(mid + 1):
#                 return mid + 1
#             elif isBadVersion(mid):
#                 high = mid
#             else:
#                 low = mid + 1
#         return low

class Solution:
    def firstBadVersion(self, n):
        low, high = 1, n

        while low < high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low