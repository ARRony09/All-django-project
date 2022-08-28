class Employee:
    no_of_leaves=8

    def __init__(self ,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"The Name is {self.name} salary is {self.salary} role is {self.role}"

harry = Employee("Harry",500,"Instructor")

# rony = Employee()
# harry = Employee()
# harry.name = "Harry"
# harry.salary = 500
# harry.role = "Instructor"
#
# print(harry.print_details())
print(harry.name)