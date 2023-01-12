import pandas as pd
data = {
    "apples": [4,2,3,6],
    "oranges": [2,3,5,1]
}
index = ["Aaron","Lee","Steve","Shaun"]
purchases = pd.DataFrame(data,index=index)
print(purchases)
print(type(purchases))
print(purchases["apples"])
print(purchases.loc["Lee"])