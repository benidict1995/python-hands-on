from pathlib import Path
import json

def favorite_number():
    path = Path("file/remember_favorite_number.json")
    save_favorite_number(path)

def read_favorite_number(path):
    if path.exists():
        contents = path.read_text()
        favorite = json.loads(contents)
        return print(f"Your favorite number is {favorite}")
    else:
        return None

def save_favorite_number(path):
    if path.exists():
       return read_favorite_number(path)
    else:
        num = input("Enter favorite number: ")
        contents = json.dumps(num)
        path.write_text(contents)
        return print(f"Save favorite number {num}")

favorite_number()