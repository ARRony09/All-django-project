def funargs(*args, **kwargs):
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


args1 = ["Harry", "Rohan", "Shivam"]
args2 = {"Rony": "python learner", "Harry": "The programmer"}
funargs(*args1, **args2)
