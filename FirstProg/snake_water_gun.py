import random
number_choice=["Water","Gun","Snake"]
number = random.choice(number_choice)
n=1
count_computer = 0
count_player = 0
while(n<11):
    user_input = str(input("Please Enter s for Snake or w for Water or g for Gun "))
    if number == "Water" and user_input == "g":
        print("You lose and Computer Win")
        count_computer = count_computer+1
        n=n+1
        continue
    elif number == "Water" and user_input == "s":
        print("You win and Computer lose")
        count_player = count_player+1
        n = n + 1
        continue
    elif number == "Water" and user_input == "w":
        print("Canceled")
    elif number == "Snake" and user_input == "g":
        print("You win and Computer lose")
        count_player = count_player + 1
        n = n + 1
        continue
    elif number == "Snake" and user_input == "s":
        print("this is cancel")
    elif number == "Snake" and user_input == "w":
        print("You lose and Computer Win")
        count_computer = count_computer + 1
        n = n + 1
        continue
    elif number == "Gun" and user_input == "g":
        print("This is cancel")
    elif number == "Gun" and user_input == "s":
        print("you lose and computer win")
        count_computer = count_computer + 1
        n = n + 1
        continue
    elif number == "Gun" and user_input == "w":
        print("You win and Computer lose")
        count_player = count_player + 1
        n = n + 1
        continue
    else:
        print("You have entered wrong value.Try again")
print(f"Your count {count_player}")
print(f"computer {count_computer}")
if count_computer>count_player:
    print("computer win this game ")
elif count_player>count_computer:
    print("You win this game ")
else:
    print("match draw")


# print(number)