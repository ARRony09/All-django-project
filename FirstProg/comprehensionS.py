# List comprehension
# ls= []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)
# ls=[i for i in range(200) if i%5==0]
# print(ls)

# dictionary comprehension

# dict1 = {i:f"{i} items"for i in range(100) }
# dict2 = {value:key for key,value in dict1.items() }
# print(dict1,"\n",dict2)

a=int(input("Enter the number of items you want \n"))
b=int(input("Enter 1 for list, 2 for dict , 3 for set \n"))
if b==1:
    list1 = [i for i in range(a)]
    print(list1)
elif b==2:
    dict1 = {i:f"item{i}"for i in range(a) if b==2}
    print(dict1)
elif b==3:
    set1 = (i for i in range(a) if b==3)
    print(set1)