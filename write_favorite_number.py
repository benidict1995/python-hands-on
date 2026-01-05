from pathlib import Path
import json

path = Path("file/favorite_number.json")
num = input("Enter your favorite number? ")
contents = json.dumps(num)
path.write_text(contents)
print(f"Save your favorite number {num}")