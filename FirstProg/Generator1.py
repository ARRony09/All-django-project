def fact(n):
    sum = 1
    for i in range(1,n):
        sum = sum*i
    yield sum

f=fact(6)
print(f.__next__())
print(f.__next__())
print(f.__next__())

# for i in f:
#     print(i)

def fibo (m):
    n1 = 1
    n2 = 1
    n3=1
    for i in range(m):
        n3=n1+n2
    return n3


