import requests
import pickle
# x = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# # print(x)
# l1 = x.split("\n")
# # print(l1)
# l2=[item.split(",") for item in l1 if len(item)!=0]
# # print(l2)
# with open ("Expkl.pkl","wb") as f:
#     pickle.dump(l2,f)

with open ("Expkl.pkl","rb") as f:
    print(pickle.load(f))