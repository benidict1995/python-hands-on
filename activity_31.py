from pathlib import Path

#1
path = Path('file/learning_python.txt')
content = path.read_text()
#print(f"{content}")

#2
path = Path('file/dog.txt')
content = path.read_text().replace('dog', 'cat')
#print(content)

#3
for line in content.splitlines():
    print(line)