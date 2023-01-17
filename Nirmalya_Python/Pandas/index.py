import pandas as pd

data = {
    "apples": [3,4,6,9],
    "bananas": [1,5,6,8]
}

index = ['a','b','c','d']

purchases = pd.DataFrame(data, index=index)
print(purchases)
print(type (purchases))

print(purchases["apples"])