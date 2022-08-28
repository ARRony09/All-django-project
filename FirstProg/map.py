# numbers = ["3","34","64"]
# numbers=list(map(int,numbers))
# numbers[1]=numbers[1]+1
# print(numbers[1])

# num=[2,3,4,5,6,7,3,3,2]
# square=list(map(lambda x: x*x,num))
# print(square)

def sq(a):
    return a*a
def cube(a):
    return a*a*a

func=[sq,cube]


for i in range(5):
    square = list(map(lambda x:x(i), func))
    print(square)

