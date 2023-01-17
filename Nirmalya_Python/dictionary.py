#dictionary
avengerDictionary = {
    "Ironman": 10,
    "Captain America": 9,
    "Thor": 8
}

print("Ironman Score = ", avengerDictionary["Ironman"])

employee = {
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
}

for emp in employee:
    print("Name: ", emp["name"])
    print("ID: ", emp["emp_id"])
    for address in emp["address"]:
        print("Pincode", address["pincode==="])

print("employee address : ", employee["address"])