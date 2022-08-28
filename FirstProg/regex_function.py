import re

# meta character \d
# txt = "That will be 596 dollers and 50 cent"
# x = re.findall("\d",txt)
# print(x)

# . Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
# txt = "hello_world "
# x = re.findall("he..o_w..ld",txt)
# print(x)

# ^ Check if the string starts with 'hello

# txt = "hello world"
#
# x = re.findall("^hello",txt)
# if x:
#     print("Yes, the string with 'hello'")
# else:
#     print("No match")

# $ check if the strimg with 'world

# txt = "hello world"

# x = re.findall("world$",txt)
# if x:
#     print("Yes")
# else:
#     print("No match")

# txt = "The rain in Spain falls mainly in the plain "
# x = re.findall("aix*",txt)
# print(x)
# if x:
#     print("yes, there is at least one match ")
# else:
#     print("no match")

# Check if the string contains "a" followed by exactly two "l" characters:

# txt = "the rain in spain falls mainly all in plain!"

# x = re.findall("a1{2}",txt)
# print(x)
# if x:
#     print("Yes there is at least one match ")
# else:
#     print("No match")

txt = "the rain in spain falls mainly all in plain!"
x=re.findall("falls|stays",txt)
print(x)
if x:
    print("Yes, there is at least one match ")
else:
    print("No match")