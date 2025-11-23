from pathlib import Path

#1
path = Path('file/guests.txt')
guestsList = ""
if path.exists():
    guests = path.read_text()
    guestsList += guests
else:
    guests = ""  # or handle it however you want

name = input("Enter your name: ")

if guests == "":
   guestsList += f"{name}"
else:
   guestsList += f",{name}"

path.write_text(guestsList)

#2
print("\nUpdated Guest List:")
counter = 0
if path.exists():
    guests = path.read_text()
    list = guests.split(",")
    for guest in list:
        counter += 1
        print(f"{counter}. {guest}")
