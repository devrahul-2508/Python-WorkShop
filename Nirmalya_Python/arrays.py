#array
array = []
for i in range(10):
    array.append(i)
print("array", array)

#input
myName = input("Please enter your name")
print("Inputed name ", myName)
print("Inputed name datatype", type (myName))

myAge = int(input("Please enter your age"))
print("Inputed age", myAge)
print("Inputed age type", type (myAge))

#5th January
#list
avengerList = ["Iron Man", "Captain America", "Thor"]
avengerScore = [90, 80, 90]
avengerDB = []
for i in range(len(avengerList)): 
    avengerDB.append(avengerList[i])
    avengerDB.append(avengerScore[i])

print(avengerList, type (avengerList))
print(avengerScore, type (avengerScore))
print(avengerDB, type (avengerDB))

#tuple
avengerTuple = ("Iron Man", "Captain America", "Thor")
print(avengerTuple[0])
print(avengerTuple[1])

#2d-array
array2D = []
for i in range(len(avengerList)):
    aTuple = (avengerList[i], avengerScore[i])
    print("Row ", i+1, aTuple)
    array2D.append(aTuple)

for i in range(len(avengerList)):
    print(avengerList[i], "\n", avengerScore[i])

print(array2D)

#2-d array accessing
avengerRatings = [
    ["SpiderMan", 8],
    ["Groot", 7],
    ["BlackWidow", 8]
]

for element in avengerRatings:
    for innerElement in element:
        print(innerElement)