from pathlib import Path
import json

user_info = {'first_name': '', 'last_name': '', 'birthday': ''}
firstName = input("Enter your Firstname: ")
lastName = input("Enter your Lastname: ")
birthday = input("Enter your Birthday: ")

user_info["first_name"] = firstName
user_info["last_name"] = lastName
user_info["birthday"] = birthday

path = Path("file/user_info.json")
contents = json.dumps(user_info)
path.write_text(contents)

print(f"User info: {user_info} is already saved!")
