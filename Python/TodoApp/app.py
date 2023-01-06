import json
from datetime import date

newDoc = False
# task = {} #init data

while(True):
    with open("todoDB.json", "r") as f:
        todoData = json.load(f) #reading todoDB.json

    keys = list(todoData.keys())
    currentDate = date.today()

    #checking for new user
    if(len(todoData) == 0):
        emptyDoc = True
        userName = input("\n Hii there! welcome to todo cli. \n Please enter your name:  ")
        todoData["name"] = userName
        todoData["date"] = str(currentDate)
        print(f"\n Hey {userName} I hope you have a great start today let's plan your day. \n Please type create task or add task to add your tasks for the day")

        cmd = input(">>") #inputing any command
        todoData["Today"] = []

        if(cmd == "create task" or cmd == "add task"):
            print("\n Please provide details about task as per the cli instruction")
            print("\n Add time in military format")

            taskDescription = input("Please enter your task description")
            scheduleTime = input("Please enter the scheduled time")

            task = {
                "description": taskDescription,
                "scheduledTime": scheduleTime
            }
            todoData["Today"].append(task)

            with open("todoDB.json", "w") as f:
                print("Please wait adding task.....")
                json.dump(todoData, f, indent=4)

            print("task added")
            continue

        elif(cmd == "break" or cmd == "close"):
            break