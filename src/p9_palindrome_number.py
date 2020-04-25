class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        return x == reverted_number or x == reverted_number // 10


test = Solution()
print(test.isPalindrome(0))
print(test.isPalindrome(12))
print(test.isPalindrome(313))
print(test.isPalindrome(556655))
print(test.isPalindrome(-3))
