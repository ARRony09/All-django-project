# class Parrot:
#     species = "bird"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # instantiate the parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)
#
# # access the class attributes
# print(f"Blu is a {blu.__class__.species}")
# print(f"Woo is a {woo.__class__.species}")
#
# # access the instance attributes
# print(f"{blu.name} is a {blu.age} years old")
# print(f"{woo.name} is a {woo.age} years old")


# creating Methods in python
class Parrot:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is dancing who's age is {self.age} "

blu = Parrot("Blu",10)
print(blu.sing("Happy"))
print(blu.dance())