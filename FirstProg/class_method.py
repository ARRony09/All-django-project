# class Employee:
#     no_of_leaves=8
#
#     def __init__(self ,aname,asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def print_details(self):
#         return f"The Name is {self.name} salary is {self.salary} role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls,new_leaves):
#         cls.no_of_leaves = new_leaves
#
#
# harry = Employee("Harry", 500, "Instructor")
# Rohan = Employee("Rohan",600,"Assistant")
#
# harry.change_leaves(34)
# print(harry.no_of_leaves)

# class method As ALternative constructors

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

# harry = Employee("Harry", 500, "Instructor")
# Rohan = Employee("Rohan",600,"Assistant")
karan = Employee.from_dash("Karan-480-Student")
print(karan.name)
