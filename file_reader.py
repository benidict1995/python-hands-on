from pathlib import Path

# path = Path('file/pi_digits.txt')
path = Path('file/pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
print(f"original: \n{contents}\n")
for line in lines:
    pi_string += line.lstrip()
    # print(line)

print(f"{pi_string[:52]}...")

