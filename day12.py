print("the number guess game ")
import random
NUM=random.randint(0,100)
print(NUM)
dificulty=input("chioce the dificulty level:")
count=1
isfinished=False
if dificulty=="easy":
    iteration=10
else:
    iteration=5
while count<=iteration and not isfinished:
    
    guess=int(input("enter your guess:"))   
    if NUM>guess:
        print("too low")
        # print("you lose")
        print(f"you have {iteration-count} left")
    elif NUM<guess:
        print("too high")
        # print("you lose")
        print(f"you have {iteration-count} left")
    elif NUM==guess:
        print("you won")
        print(f"you got it the answer is {NUM}")
        isfinished=True
    
    count+=1
    if count>iteration:
        print("you do not guess any more,you lose the game")
   

    


