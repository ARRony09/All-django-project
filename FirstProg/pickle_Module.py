import pickle

# create pickle file
# cars = ["Audi", "BMW","Toyota","Hammer"]
# file = "mycar.pkl"
# fileobj = open(file, "wb")
# pickle.dump(cars, fileobj)
# fileobj.close()

# retrive file

# file="mycar.pkl"
# file_obj = open(file,"rb")
# my_car = pickle.load(file_obj)
# print(my_car)
# print(type(my_car))

file_ob = open("mycar.pkl","rb")
rawdata = file_ob.read()

my_ob=pickle.loads(rawdata)
print(my_ob)