# class Solution:
#     def binaryGap(self, N: int) -> int:
#         binary_string = ''
#         while N:
#             last_digit = N % 2
#             binary_string += str(last_digit)
#             N >>= 1
#         flag = max_gap = 0
#         binary_string = binary_string[::-1]
#         for i in range(len(binary_string)):
#             if binary_string[i] == '1':
#                 max_gap = max(max_gap, i - flag)
#                 flag = i
#         return max_gap


class Solution:
    def binaryGap(self, N: int) -> int:
        last, max_gap = -1, 0
        for i in range(32):
            if (N >> i & 1) >= 1:
                if last >= 0:
                    max_gap = max(i - last, max_gap)
                last = i
        return max_gap
