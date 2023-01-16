# print("adding the two number of the digit ")
# two_digit_num=input("enter the two digit number\n")
# first_num=int(two_digit_num[0])
# second_num=int(two_digit_num[1])
# total=first_num+second_num
# print("The sum of number is "+str(total))
# body mass index calculator//////////////////////////////////////////////////////////
# height=input("Enter your height in m:")
# weight=input("Enter your weight in kg :")
# height_float=float(height)
# weight_float=float(weight)
# bmi=weight_float/(height_float**2)
# print("The bmi is : "+str(round(bmi)))
# print("The bmi is : "+str((bmi)))

# this is the code to calculate the day ,week and month in the remaining year///////////////////
# year=90-int(input("enter your age\n"))
# print(year)
# day=year*365
# week=year*52
# month=year*12
# print(f"The remaining day is :{day},the week is :{week} and the month is:{month}")
# tip calculator///////////////////////////////////////////////////////////////////// 
# total=input("enter the total bill:$")
# percentage=input("enter the prsent do you want to give:")
# person=input("enter the number of your friends:")
# bill_foreach=(int(total)+(int(percentage)*int(total))/100)/int(person)
# print(f"The bill for each person is:${bill_foreach}")
# even or odd checking up/////////////////////////////////////////////////////
number=input("Enter the number :")
if int(number)%2==0:
    print(f"The number {number} is even number")
else:
    print(f"The number {number} is odd number")