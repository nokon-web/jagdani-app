import random
# row1=[" "," "," "]
# row2=[" "," "," "]
# row3=[" "," "," "]
# map=[row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position=input("enter the position you want to put x:")
# a=int(position[0])
# b=int(position[1])
# map[a-1][b-1]="X"
# print(f"{row1}\n{row2}\n{row3}")
# GAME /////////////////////////////////////////////////////////////////
rock=['''[////////)/////)]\n
                   /////)\n
                   ////////)\n
                ///////)\n''']

paper=['''~~~~~~)~~~~~~)\n
                   ~~~~~~)\n
                   ~~~~~~)\n
                ~~~~~~)\n''']
scissor=['''))))))))(((((()))))))\n
                   )))))))))))\n
                   (((((()))))))\n
                ))))))))))))''']
# print(rock,paper,scissor)
choice=[rock,paper,scissor]
computer_choice=random.randint(0,2)
your_choice=input("Enter number:")
if int(your_choice)==0:
    print("your choice\n")
    print(rock)
    print("computer choice\n")
    print(choice[computer_choice])
elif int(your_choice)==1:
    print("your choice\n")
    print(paper)
    print("computer choice\n")
    print(choice[computer_choice])
else:
    print("your choice\n")
    print(scissor)
    print("computer choice\n")
    print(choice[computer_choice])
if int(your_choice)==computer_choice:
    
    # print(choice[computer_choice])
    print("you won")
else:
    print("you loss")





