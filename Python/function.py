#simple function multiply two numbers
def multiply(number1, number2):
    mul = number1 * number2
    print("Multiplication Result Inside function body", mul)
    return mul
    
result = multiply(10, 20) #coment when called from main
print("Multiplication Result Outside function body", result) #coment when called from main

employee = [{
    "name": "Tony Stark",
    "emp_id": 3,
    "address": [
        {
            "line1": "line1 address",
            "line2": "line2 address",
            "state": "state address",
            "pincode": 712258
        },
        {
            "line1": "2line1 address",
            "line2": "2line2 address",
            "state": "2state address",
            "pincode": 2712258
        }
    ]
}]

#fetch from employee
def fetchEmployeeAddress(employeeList, addressKey):
    emp_pin_list = []
    for emp in employeeList:
        emp_pin_list.append({"name": emp["name"]})
        emp_pin_list[employeeList.index(emp)][addressKey] = []
        for address in emp["address"]:
            emp_pin_list[employeeList.index(emp)][addressKey].append(address[addressKey])
    return emp_pin_list

result = fetchEmployeeAddress(employee, "pincode") #coment when called from main
print(result) #coment when called from main