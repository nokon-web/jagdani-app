class Solution:
    def romanToInt(self,s):
        # s=input("enter the number :")
        isfinished=False
        while not isfinished:    
            toInt={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
            for i in range(0,len(s)):
                for j in toInt:
                    sum=0 
                    count=0
                    if s[i]==j:
                        sum+=toInt[j]
                        count+1
                        if count==len(s):
                            isfinished=True
                            return sum
                            

print(Solution().romanToInt())
