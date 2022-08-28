import json
# x = '{ "name":"John", "age":30, "city":"New York"}'
# # parsed x
# y = json.loads(x)
# print(y["age"])

# json.dumps
x = {
    "name" : "jhon",
    "age" : 30,
    "city" : "New York"
}

y = json.dumps(x)
print(y)