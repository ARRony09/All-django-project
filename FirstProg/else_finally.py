
try:
    f=open("Rony.txt")

except Exception as e:
    print(e)
else:
    print("if except is not running then it will enter into else")

finally:
    print("Now code is completed")
    f.close()
