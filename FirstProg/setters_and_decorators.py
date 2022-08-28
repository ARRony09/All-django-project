class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return ("Email is not set")
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):

        print("Setting now ")
        names = string.split("@")[0]
        self.fname =names.split(".")[0]
        self.lname =names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

Bangladeshi_supporter = Employee("Bangladeshi","supporter")
print(Bangladeshi_supporter.email)
Bangladeshi_supporter.fname="US"
print(Bangladeshi_supporter.email)
# Bangladeshi_supporter ="This.that@gmail.com"

Bangladeshi_supporter.email = "This.that@gmail.com"
print(Bangladeshi_supporter.lname)

del Bangladeshi_supporter.email
print(Bangladeshi_supporter.email)