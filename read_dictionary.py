from pathlib import Path
import json

path = Path("file/user_info.json")
contents = path.read_text()
userInfo = json.loads(contents)
print(f"User Info: {userInfo}")