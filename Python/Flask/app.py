from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {
        "user_id": 1,
        "username": "user1"
    },
    {
        "user_id": 2,
        "username": "user2"
    }
]

@app.route('/hello')
def hello():
    print("I am in the hello route")
    return "Hello"

@app.route('/get_all_user_id')
def get_all_user_id():
    userId = []
    for user in users:
        obj = {}
        obj['user_id'] = user['user_id']
        userId.append(obj)
    return jsonify(userId)

@app.route('/get_all_user_name')
def get_all_user_name():
    userName = []
    for user in users:
        obj = {}
        obj['username'] = user['username']
        userName.append(obj)
    return jsonify(userName)

if(__name__ == '__main__'):
    app.run(host='127.0.0.1', port='3000', debug=True)