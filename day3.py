# body mass index calculator//////////////////////////////////////////////////////////
# height=input("Enter your height in m:")
# weight=input("Enter your weight in kg :")
# height_float=float(height)
# weight_float=float(weight)
# bmi=weight_float/(height_float**2)
# print("The bmi is : "+str(round(bmi,1)))
# if bmi<=18.5:
#     print("you are underweight")
# elif bmi<=25:
#     print("you have normal weight")
# elif bmi<=30:
#     print("your are overweight")
# else:
#     print("you must go to clinic unless there is risk on you")
# To check whether the is leap year or not ////////////////////////////////
# year=int(input("Enter the year :"))
# print(year%4)
# print(year%100)
# print(year%400)
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(f"The year you entered is leap year")
#         else:
#             print(f"The year you entered is  not leap year")
#     else:
#         print(f"The year you entered is leap year")
# else:
#     print(f"The year you entered is  not leap year")

# the ticket program/////////////////////////////////////////////////////////////////////////////
# height=int(input("enter the height:"))
# bill=0
# if height>=120:
#     print("you can ride")
#     age=int(input("enter your age"))
#     if age<=12:
#         bill=5
#         add_photo=input("enter yes or no:")
#         if add_photo=="Y":
#             print(f"the bill is {bill+3}")
#         else:
#            print(f"your ticket is {bill}")
#     elif age<=18:
#         bill=7
#         add_photo=input("enter yes or no:")
#         if add_photo=="Y":
#             print(f"the bill is {bill+3}")
#         else:
#            print(f"your ticket is {bill}")
       
#     else:
#         bill=12
#         add_photo=input("enter yes or no:")
#         if add_photo=="Y":
#             print(f"the bill is {bill+3}")
#         else:
#            print(f"your ticket is {bill}")
# else:
#     print("sorry ,you can't ride")     
# love calculator///////////////////////////////////////////////
# myname=input("enter your name:")  
# hername=input("enter her name:") 
# concate=myname+hername
# print(concate)
# t=concate.count("t")
# r=concate.count("r")
# u=concate.count("u")
# e=concate.count("e")
# print(t,r,u,e)
# true=t+r+u+e
# print(true)
# l=concate.count("l")
# o=concate.count("o")
# v=concate.count("v")
# e=concate.count("e")
# print(l,o,v,e)
# love=l+o+v+e
# print(love)
# percent_love=str(true)+str(love)
# print(f"The love percentage between you and your girl freinds is {percent_love}%")
# treasure game/////////////////////////////////////////////////////////////////
print("this is the treasure game \n in the island")
direction=input("chioce the direction that you must go and find that resource:")
if direction=="left":
    way=input("by what mean you to there:")
    if way=="boot":
        chioce_home=input("Enter the color of home that you want :")
        if chioce_home=="red":
            print("game_over")  
        elif chioce_home=="yellow":
            print("you won the game")
        else:
             print("game_over")  
    else:
         print("game_over") 

else:
   print("game_over")        

