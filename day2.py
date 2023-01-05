avengerList = ["IronMan","Captain America","Thor"]
ratingList = [10,9,8]

totalList =[]


for j in range(len(avengerList)):
    totalList.append(avengerList[j])
    totalList.append(ratingList[j])

print(totalList)    
print(totalList[-1])
print(totalList[-2:])

avengerTuple = ("Iron Man","CaptainAmerica")
#avengerTuple[0]="Batman"
#print(avengerList,type(avengerList))

twodlist=[]

for i in range(len(avengerList)):
    aTuple = [avengerList[i],ratingList[i]]
    twodlist.append(aTuple)
   
print(twodlist)   

ratedAvengerList2D=[
    ['IronMan', 10], ['Captain America', 9], ['Thor', 8]
]

for i in range(0,len(ratedAvengerList2D)):
    for j in range(0,len(ratedAvengerList2D[i])):
        print(ratedAvengerList2D[i][j])
    

for elem in ratedAvengerList2D:
    print(elem)
    for innerelem in elem:
        print(innerelem)

avengersDict = {
    "Ironman":10,
    "Captain America": 9,
    "Thor":8
}
print("IronMan'S Score",avengersDict["Ironman"])




employeeList = [
            {
    "name": "Tony Stark",
    "emp_id": 3,
    "address":[
        {
            "line1":"fff",
            "line2":"hh",
            "state": "WB",
            "pincode":"700107"
        },
        {
            "line1":"fff",
            "line2":"hh",
            "state": "Maharashtra",
            "pincode":"600120"
        }
    ]
},
{
 "name": "Batman",
    "emp_id": 3,
    "address":[
        {
            "line1":"fff",
            "line2":"hh",
            "state": "WB",
            "pincode":"700107"
        },
        {
            "line1":"fff",
            "line2":"hh",
            "state": "Maharashtra",
            "pincode":"600120"
        }
    ]
}]
    
emp_pin_list = []
for emp in employeeList:
        print(emp['name'])
        print("ID",emp["emp_id"])
        emp_pin_list.append({"name":emp["name"]})
        emp_pin_list[employeeList.index(emp)]['pincode']=[]

        for address in emp["address"]:
            print(employeeList.index(emp))
            emp_pin_list[employeeList.index(emp)]['pincode'].append(address['pincode'])

print(emp_pin_list)
emp_pin={}
emp_pin['employee_name'] = 'Tony'
print(emp_pin)
