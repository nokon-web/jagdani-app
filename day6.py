# def sum():
#     num1=input("enter number 1:\n")
#     num2=input("enter number 2:\n")
   
#     result=int(num1)+int(num2)
#     return result
#     # print(result)
# print(sum())
# my game//////////////////////////////////////////////////////////////////
num=6
lists=["*","*","*","*","*"]
concate=""
while num>0:
    def increment():
        for n in range(0,len(lists)):
            concate+=lists[n]
            return concate
    num-=1 
    def decrement():
        for n in range(0,len(lists)):
            concate+=lists[n]
            return concate
    num+=1
    if num>6:
        increment()
    else:
        decrement()


    
    