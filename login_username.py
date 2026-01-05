from pathlib import Path
import json


def login_user():
    path = Path("file/user_info.json")
    contents = path.read_text()
    userInfo = json.loads(contents)
    username = userInfo["username"]
    password = userInfo["password"]
    fname = userInfo["first_name"]
    lname = userInfo["last_name"]
    
    entUsername = input("Enter username: ")
    entPassword = input("Enter password: ")

    if entUsername == username and entPassword == password:
        print(f"Welcome {fname} {lname}")
    else: 
        print(f"Invalid username or password")
        login_user()

login_user()