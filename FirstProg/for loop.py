# list1 = [2,3,4,10,29,83,28]
# for i in list1:
#     if i and i>6:
#         print(i)
#
# while(True):
#     inp = input("Enter a value ")
#     if int(inp)>100:
#         print("nice")
#         break
#     else:
#         print("Try Again")
#         continue
#

# Guess game
# i=0
# n=18
# while(i<9):
#     inp=input("enter the number ")
#     if int(inp)== n:
#         print("congratulation, you win")
#         break
#     elif int(inp)> n:
#         print("Number is Too big,try again")
#         i = i + 1
#         continue
#     elif int(inp)< n:
#         print("Number is too small,try again")
#         i = i + 1
#         continue
#     else:
#         print("Enter worng word")
# def hello(l):
#     """This is for checking doc string"""
#     return 1
# print(hello.__doc__)

# Try except
# print("Enter Num 1 ")
# num1=input()
# print("Enter num 2 ")
# num2 = input()
# try:
#     print("The sum of these two numbers is ",int(num1)+int(num2))
# except Exception as e:
#     print(e)
#
# print("This line is very important ")


# Astrologer's star
i = 0
j = 0
n = int(input("Enter your number "))
inp = int(input("Enter 1 or 0 "))
if inp == 1:
    for i in range(0,n):
        for j in range(i+1):
            print("*", end=" ")
        print("\r")
elif inp == 0:
    for i in range(n, 0, -1):
        for j in range(i+1):
            print("*", end=" ")
        print("\r")
else:
    print("Wrong")

# l = 10
#
#
# def function1(n):
#     # l=5
#     m = 8
#     global l
#     l = l + 5
#     print(l, m)
#     print(n)
#
#
# function1("This is Rony")
# print(l)
