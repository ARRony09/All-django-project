def getdate():
    import datetime
    return datetime.datetime.now()


print("Enter your name ")
print("1.Rohan ")
print("2.Harry ")
print("3.Hammad ")
n = int(input("Enter your number "))


def take(input1):
    if input1 == 1:
        input2 = int(input("press 1 Rohan exercise or press 2 Rohan Food "))
        if input2 == 1:
            value = str(input("Type here\n"))
            with open("Rohan-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully Written")
        elif input2 == 2:
            value = str(input("Type here\n"))
            with open("Rohan-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully Written")
        else:
            print("Wrong value. please enter correct value ")

    elif input1 == 2:
        input2 = int(input("press 1 Harry exercise or press 2 Harry Food "))
        if input2 == 1:
            value = str(input("Type here\n"))
            with open("Harry-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully Written")
        elif input2 == 2:
            value = str(input("Type here\n"))
            with open("Harry-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully Written")
        else:
            print("Wrong value. please enter correct value ")

    elif input1 == 3:
        input2 = int(input("press 1 Hammad exercise or press 2 Hammad Food "))
        if input2 == 1:
            value = str(input("Type here\n"))
            with open("Hammad-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully Written")
        elif input2 == 2:
            value = str(input("Type here\n"))
            with open("Hammad-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully Written")
        else:
            print("Wrong value. please enter correct value")


def retrieve(input1):
    if input1 == 1:
        input2 = int(input("press 1 Rohan exercise or press 2 Rohan Food "))
        if input2 == 1:
            with open("Rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif input2 == 2:
            with open("Rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("Wrong value. please enter correct value")

    elif input1 == 2:
        input2 = int(input("press 1 Harry exercise or press 2 Harry Food "))
        if input2 == 1:
            with open("Harry-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif input2 == 2:
            with open("Harry-food.txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("Wrong value. please enter correct value ")

    elif input1 == 3:
        input2 = int(input("press 1 Hammad exercise or press 2 Hammad Food "))
        if input2 == 1:
            with open("Hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif input2 == 2:
            with open("Hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("Wrong value. Please enter correct value")
    else:
        print("Sorry you press wrong value")


print(take(n))
print((retrieve(n)))
