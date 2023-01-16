computer_guess="melkamu"
print(computer_guess)
print(len(computer_guess))
underscore=[]
for n in range(0,len(computer_guess)):
    underscore+="_"
        
        
print(underscore)
guess=input("guess the letter:")
for n in computer_guess:
    if n==guess:
        underscore[n]=guess
        print(underscore)
    else:
        underscore[n]="_"
        print(underscore)

# # print(underscore)
# for i in underscore:
#     if i=="_":
#         continue
#     else:
#         print(guess)



