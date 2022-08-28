# single inheritance

# class Employee:
#     no_of_leaves = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def print_details(self):
#         return f"The Name is {self.name} salary is {self.salary} role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls, new_leaves):
#         cls.no_of_leaves = new_leaves
#
#     @classmethod
#     def from_dash(cls, string):
#         # params = string.split("-")
#         # print(params)
#         # return cls(params[0], params[1], params[2])
#         return cls(*string.split("-"))
#
#     @staticmethod
#     def printgood(string):
#         print(f"This is {string}")
#
#
# # harry = Employee("Harry", 500, "Instructor")
# # Rohan = Employee("Rohan",600,"Assistant")
# # karan = Employee.from_dash("Karan-480-Student")
# # print(karan.name)
# # Employee.printgood("Rony")
#
# class programer(Employee):
#     def __init__(self):
#         super.__init__(self,aname, asalary, arole,language)
#         self.language = language
#
#
#     def printprog(self):111
#         return f"The programmer's Name is {self.name} and languge is {self.language}"
#
# Rony= programer("Rony",555,"Student",["python"])
# print(Rony.language)

# multiple Inheritance
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"The Name is {self.name} salary is {self.salary} role is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

    @staticmethod
    def print_good(string):
        print(f"This is {string}")

class player:
    def __init__(self,name,game):
        self.name = name
        self.game = game
    def print_details(self):
        return f"The name is {self.name},Game is {self.game}"

class cool_programer(Employee,player):
    language="c++"
    def print_language(self):
        print(self.language)
        

Rony = player("Rony","GTA5")
Sazzad = cool_programer("Karan",5559,"instructor")
print(Sazzad.print_details())
print(Rony.print_details())
print(Sazzad.print_language())