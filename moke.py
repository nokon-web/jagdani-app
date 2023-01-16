class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        

        x_revesed=int(str(x)[::-1])

        if x==x_revesed:
                return True
        elif x!=x_revesed and x<0:
            return False
x=-121
print(Solution().isPalindrome(x))
