from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def greet_user():
    """Greet the user by name."""
    path = Path('file/username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back {username}!")
    else:
        username = input("what is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)

        print(f"We'll remember you when you come back, {username}!\n")


greet_user()

