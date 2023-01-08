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
                "scheduledTime": scheduleTime,
                "status": "TBD"
            }
            todoData["Today"].append(task)

            with open("todoDB.json", "w") as f:
                print("Please wait adding task.....")
                json.dump(todoData, f, indent=4)

            print("task added")
            continue

        elif(cmd == "break" or cmd == "close"):
            break

    if("Today" in list(todoData.keys())):
        tasks = todoData["Today"]
        userName = todoData["name"]
        print(f"\n Today is {currentDate}")
        print(f"\n Hey {userName} here are all your task for the day.")
        for task in tasks:
            print("\n Task Id: ", tasks.index(task))
            print("\n Task Description:  ", task["description"])
            print("\n Schedule Time:  ", task["scheduledTime"])

        print("\n For adding more task please type <create tasks> or <add tasks>")
        print("\n For deleting the current user type <delete user>")
        print("\n For deleeing all tasks please type <delete all tasks>")
        print('\n For task status change type <change status>')
        print("\n For Exiting from the app type <done> or <exit>")
        cmd = input(">>")

        if(cmd == "create task" or cmd == "addd task"):
            taskDescription = input("Please enter task desription")
            scheduleTime = input("Please enter schedule time")

            task = {
                "description": taskDescription,
                "scheduledTime": scheduleTime,
                "status": "TBD"
            }
            todoData["Today"].append(task)

            with open("todoDB.json", "r+") as f:
                f.seek(0)
                json.dump(todoData, f, indent=4)
            
            print("\n Task created successfully.")
            print("\n type <create task> or <add task> to add more tasks.")
            print("\n type <done> or <exit> to exit from the app.")
            continue
        
        elif(cmd == "delete user"):
            todoData = {}

            with open("todoDB.json", "w") as f:
                f.seek(0)
                json.dump(todoData, f, indent=4)
            
            print("\n User deleted successfully")
            continue

        elif(cmd == "delete all tasks"):
            todoData["Today"] = []

            with open("todoDB.json", "w") as f:
                print("\n All tasks deleted successfully.")
                json.dump(todoData, f, indent=4)
            
            continue

        elif(cmd == "change status"):
            tasks = todoData["Today"]
            if(len(tasks) > 0):
                taskId = input("Please enter task id:  ")
                array = []

                if(int(taskId) < len(tasks)):
                    for element in tasks:
                        if(int(taskId) == tasks.index(element)):
                            element["status"] = "DONE"
                        array.append(element)  

                    with open("todoDB.json", "w") as f:
                        todoData["Today"] = array
                        print("\n Status changed successfully.")
                        json.dump(todoData, f, indent=4)                          
                else: 
                    print("Invalid task id")
            else: 
                print("No tasks exists")

        elif(cmd == "done" or cmd == "exit"):
            break