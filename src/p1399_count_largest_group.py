class Solution:
    def countLargestGroup(self, n: int) -> int:
        group = [0] * 36
        for i in range(1, n + 1):
            group[self.sum_of_digits(i) - 1] += 1
        max_sum_of_digits = count = 0
        for num in group:
            if num > max_sum_of_digits:
                max_sum_of_digits = num
                count = 1
            elif num == max_sum_of_digits:
                count += 1
        return count

    def sum_of_digits(self, n: int) -> int:
        result = 0
        while n:
            result += n % 10
            n //= 10
        return result
