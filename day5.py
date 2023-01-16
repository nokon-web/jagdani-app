# average calculation/////////////////////////////////////////////////////////////////////////////////////
# heights=[167,157,170,180,190,200,178]
# sum=0
# count=0
# for height in heights:
#     sum+=height
#     count+=1
# average=sum/count
# print(sum)
# print(count)
# print(average)
# to check the height score///////////////////////////////////////////////////////////////////////////////////
# student_score=input("enter the score of student:").split()
# for i in range(0,len(student_score)):
#     student_score[i]=int(student_score[i])
# print(student_score)
# # student_score=[80,81,50,34,99,82]
# highest_score=0
# for score in student_score:
#     if  score>highest_score:
#         highest_score=score
# print(f"the highest score in the class is :{highest_score}")   
# fizz buzz ////////////////////////////////////////////////////////////////////////////////////////////
# for number in range(0,101):
#     if number%3==0 and number%5==0:
#         print("fizz buzz")
#     elif number%3==0:
#         print("fizz")
#     elif number%5==0:
#         print("buzz")
#     else:
#         print(number)
# password generator///////////////////////////////////////////////////////////////////
import random
letter=['a','b','c','d','e']
symbol=['@','/','#']
number=["1", "2" ,"3" ,"4" ,"5", "6", "7" ]
password=""
print("the password generator game")
letter_tot=int(input('Enter the number of letter you want:\n'))
symbol_tot=int(input('Enter the number of symbol you want:\n'))
number_tot=int(input('Enter the number of number you want:\n'))
random_char=""
for i in range(0,letter_tot):
    random_char+=random.choice(letter)
for i in range(0,symbol_tot):
    random_char+=random.choice(symbol)
for i in range(0,number_tot):
    random_char+=random.choice(number)

print(random_char)
for i in range(0,len(random_char)):
    password+=random.choice(random_char)
print(password)