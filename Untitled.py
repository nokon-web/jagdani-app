class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
x = -121

print(Solution().isPalindrome(x))