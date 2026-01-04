from pathlib import Path
import json


path = Path('file/username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("what is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)

    print(f"We'll remember you when you come back, {username}!\n")

