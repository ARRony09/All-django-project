# f = open("Rony2.txt", "a")
# f.write("Rony is a good boy \n")
# f.close()
# f = open("Rony2.txt", "r+")
# print(f.read())
# f.write("thank you")

# seek and tell function
# f = open("Rony.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.seek(5)
# print(f.tell())
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# f.close()

# with block

with open("Rony.txt") as f:
    a = f.read()
    print(a)
