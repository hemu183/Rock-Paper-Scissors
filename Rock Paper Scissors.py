import random
user_choice =int(input("enter 0 for rock,1 for paper, 2 for scissors"))
computer_choice = random.randint(0,2)
print(user_choice)
print(computer_choice)
if user_choice>=3 or user_choice<0:
    print("Invalid")
else:
    if user_choice==0 and computer_choice==2:
        print("You Win!")
    elif computer_choice==0 and user_choice==2:
        print("You Lose!")
    elif computer_choice>user_choice:
        print("You Lose!")
    elif user_choice> computer_choice:
        print("you Win!")
    elif user_choice==computer_choice:
        print("Tie")

