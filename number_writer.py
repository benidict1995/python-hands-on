from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 3]
path = Path('file/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)