def recursive(n):
    if n == 1:
        return 1
    else:
        return n * recursive(n - 1)


inp = int(input("Enter the value "))
print("Total recursive value is ", recursive(inp))


def iteraive(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
    return fact


print("Total iterative value is ", iteraive(inp))


def fabocacci(n):
    fab = 1
    for i in range(n):
        fab = fab + (i)
        return fab
    print(fab)


print("Total fabonacci value is ", fabocacci(inp))
