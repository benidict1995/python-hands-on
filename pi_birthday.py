from pathlib import Path

path = Path('file/pi_million_digits.txt')
con = path.read_text()
lines = con.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

# print(f"{pi_string[:52]}...")
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


#from pathlib import Path
# # path = Path('file/pi_digits.txt')
# path = Path('file/pi_million_digits.txt')
# contents = path.read_text()
# lines = contents.splitlines()
# pi_string = ''
# print(f"original: \n{contents}\n")
# for line in lines:
#     pi_string += line.lstrip()
#     # print(line)

# print(f"{pi_string[:52]}...")