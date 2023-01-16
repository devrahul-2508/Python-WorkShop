from flask import Flask

app = Flask(__name__)

users = [
    {
        "user_id": 1,
        "username": "user1"
    },
     {
        "user_id": 2,
        "username": "user2"
    },
     {
        "user_id": 3,
        "username": "user3"
    },
] 

@app.route('/hello')
def hello():
    print("I am in hello endpoint")
    return "hello"

@app.route('/userid')
def fetchUserIds():
    userIds=[]
    obj={}
    for user in users:
        print(user['user_id'])
        userIds.append(user["user_id"])
    obj["ids"] = userIds
    return obj

@app.route('/usernames')
def fetchUserName():
    usernames = []
   
    for user in users:
        obj={}
        obj["username"]=user["username"]
        usernames.append(obj)
  
    return usernames 



if __name__ == '__main__':
    app.run(host='127.0.0.1',port='3000',debug = True)
    print("Server is running")