class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, sum = 1, 0
        while n:
            last_digit = n % 10
            product *= last_digit
            sum += last_digit
            n //= 10
        return product - sum


print(Solution().subtractProductAndSum(234))
print(Solution().subtractProductAndSum(4421))