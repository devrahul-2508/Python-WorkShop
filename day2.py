avengerList = ["IronMan","Captain America","Thor"]
ratingList = [10,9,8]

totalList =[]


for j in range(len(avengerList)):
    totalList.append(avengerList[j])
    totalList.append(ratingList[j])

print(totalList)    
print(avengerList,type(avengerList))