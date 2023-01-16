# num=[2,7,11,15]
# def twosum():

#     for i in range(0,len(num)):
#         # print(num[i])
#         for j in range(0,len(num)):
#             # print(num[j])
#             if num[i]+num[j]==9:
#                 print(i,j)
#                 return
            
# twosum()



# number=input("enter the number :")
# reversed=""
# toNumber=int(number)
# if toNumber<0:
#     print("Negative numbers are not palindrome number")
# else:


# for i in range(0,len(toNumber)):
#         a=len(toNumber)-i
#         # print(number[a-1])
      
#         reversed+=number[a-1]
#         print(reversed)
#     reversedNumber=int(reversed)
#     if toNumber==reversedNumber:
#         print(f"The number  is the palindrome number ")
#     else:
#         print("It is not")


# longest common prefix in the array 

# class Solution:
#     def longestCommonPrefix(self, strs):
#         prifix=""
#         item=[]
#         for i in range(0,len(strs)):
#             # print(strs[i])
#             for j in range(0,len(strs[i])):
#                 x=strs[i][j]
               
#                 if  x==strs[i+1][j]:
#                     x=strs[i+1][j]
#                     prifix+=x
#                 else:
#                     prifix=""
                    
#                 # prifix+=strs[i][j]
#                 # print(prifix)
                
# strs=["melkamu","mebratu","getachew","challa"]    
# print(Solution().longestCommonPrefix(strs))




# class Solution:
#     def romanToInt( ):
#         s=input("enter the number :")
#         isfinished=False
#         while not isfinished:    
#             toInt={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#             for i in range(0,len(s)):
#                 for j in toInt:
#                     sum=0 
#                     count=0
#                     if s[i]==j:
#                         sum+=toInt[j]
#                         count+1
#                         if count==len(s):
#                             print(sum)
#                             isfinished=True
                            

# Solution().romanToInt()

                
# valid parentheses///////////////////////////////////////////////////////////////////////////
# class Solution:
#     def isValid(self, s: str) -> bool:
#         for i in range(0,len(s)):
#             iscontinue=True
#             while iscontinue:
#                 if s[i]=="(" and s[i+1]==")":
#                     return True
                
#                 elif s[i]=="[" and s[i+1]=="]":
#                      return True
                
#                 elif s[i]=="{" and s[i+1]=="}":
#                      return True

#                 else:
#                     return False
#                     iscontinue=False
# print(Solution().isValid("{}"))
# Merge Two Sorted Lists//////////////////////////////////////////////////////////////////
list1=[6,8,3,4,5,2]
list2=[2,5,7,8,0,3,5]
mergedList=[]
for i in range(0,len(list1)):

    mergedList.append(list1[i])
for i in range(0,len(list2)):

    mergedList.append(list2[i])
sortedList=mergedList.sort()
print(mergedList)
print(sortedList)

