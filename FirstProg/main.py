# input1=input()
# input2=input()
# print(f"Total is {int(input1)+int(input2)}")
# strmy =("hello friend")
# # print(len(strmy))
# # print(strmy[5::-1])
# print(strmy.endswith("friend"))
# print(strmy.count("e"))
# print(strmy.capitalize())
# print(strmy.find("e"))
# print(strmy.upper())
# print(strmy.lower())
# list=[8,9,10,5,50]
# list.sort()
# list1=[]
# list.reverse()
# list.remove(50)
# list.insert(2,49)
# list1.append(72)
# list1.append(92)
# list1.append(91)
# print(list1)
# list1.pop()
# print(list1)
# tuple = (1,2,3)
# print(tuple)
# a=1
# b=8
# a,b=b,a
# print(a,b)
# vowel_string = 'aeiou'
# print(list(vowel_string))
# vowel_tuple=('a','e','i','o','u')
# print(list(vowel_tuple))

# list

# language = ['French', 'English', 'German']
# language1 = ['Spanish', 'Portuguese']
# language.extend(language1)
# language_tuple = ('Arabic', 'Japanese')
# language.extend(language_tuple)
# language_set = {'Chinese', 'japanese'}
# language.extend(language_set)
# print('Language list: ', language)

# Dictionaries

#
# d1 = {}
# d2 = {"Harry": "Burger",
#       "Rony": "Green Tea",
#       "Jahid": "Coffee",
#       "Hasib": {"Brown Tea", "burger", "Junk food"}
#       }
# print(d2["Harry"])
# d2["Shanto"] = "Junk food"
# # d2[420] = "Pizza"
# #
# # del d2[420]
# # print(d2)
# # d3=d2.copy()
# # del d2[" Shanto "]
# # print(d2)
# # print(d3)
# # print(d2.get("Harry"))
# d2.update({"lenn":"Fish"})
# print(d2.items())
# dic={"Fish":"mach",
#      "Chicken":"murgi",
#      "beef":"Gorur gosto",
#      "Rice":"Vat"
#      }
# inp=input("Enter a word ")
# print(dic[inp])

# set_function
# my_set={1,3}
# a=set()
# print(type(a))
# my_set = {1, 3}
# # print(my_set)
# my_set.add(2)
# # print(my_set)
# my_set.update([2, 3, 4])
# print(my_set)
# my_set.update([4,5], {1,6,8})
# print(my_set)
# my_set.discard(7)
# print(my_set)

# set operation
# set Union
A= {1,2,3,4,5}
B= {4,5,6,7,8}
# print(A|B)
# print(A.union(B))
# print(B.union(A))
# set_intersection
# print(A&B)
# print(A.intersection(B))

# set difference
# print(A-B)

# symmetric Difference

# print(A^B)
# print(A.symmetric_difference(B))

# if else problem

# inp = int(input("What is your age "))
# if inp > 18:
#     print("You can drive ")
# elif inp == 18:
#     print("Please come to our office")
# else:
#     print("You can't drive")

first_input=input("Enter your operator +/-/*// ")
num1=int(input("enter the value 1st "))
num2=int(input("Enter the value 2nd "))
def Faulty(l,n1,n2):

    if l == '+':
        if n1==56 and n2==9:
            print("77")
        else:
            return (n1+n2)
    elif l == '*':
        if n1==45 and n2==3:
            print("555")
        else:
            return(n1 * n2)
    elif l == '/':
        if n1==56 and n2==6:
            print("4")
        else:
            return (n1/n2)
    elif l == '-':
        return (n1-n2)

    else:
        print("Incorrect keywords")
Faulty(first_input,num1,num2)