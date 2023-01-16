# student_score={
#     "melkamu":92,
#     "chala":80,
#     "kebede":90,
#     "ojulu":70,
#     "aldo":60
# }
# grading={}

# for key in student_score:
#     print(key)
#     grading+=key
#     print(grading)
#     key1=key
#     if student_score[key]>90:
#         print("outstanding")
#     elif student_score[key]>80:
#         print("exceeds expectation")
#     elif student_score[key]>70:
#         print("acceptable")
#     else:
#         print("fail")
# for key in student_score:
#     grading[key]=key1
# writting the code auction 
import art
import replit

print(art.photo)
list_of_people={}
highest=0
name=input("Enter your name :")
price=int(input("Enter the price you pay:"))
list_of_people[name]=price
# print(list_of_people)
is_another=input("enter yes/no:")

while is_another=="yes":
    if is_another=="yes":
        name=""
        price=""
    name=input("Enter your name :")
    price=int(input("Enter the price you pay:"))
    list_of_people[name]=price
    # print(list_of_people)
    is_another=input("enter yes/no:")
    

    if is_another== "no":
        for n in list_of_people:
           if highest<list_of_people[n]:
                highest=list_of_people[n]
                # print(f"{n} is the winner and he pay ${highest}")


# for n in list_of_people:
#         if highest<list_of_people[n]:
#             highest=list_of_people[n]
#             print(f"{n} is the winner and he pay ${highest}")

print(f"{n} is the winner and he pay ${highest}")




    