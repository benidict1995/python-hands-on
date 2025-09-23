#1
usernames = ['naruto', 'hinata', 'boruto', 'sasuke', 'sakura', 'sarada', 'admin']
for username in usernames:
    if username == 'admin':
        print(f"#1 Hello {username}, would you like to see a status report?")
    else:
        print(f"#1 Hello {username}, thank you for logging in again.")

print("\n\n")
#2
fruits = ['apple']
if fruits == []:
    print("#2 We need to find some fruits!")
else:
    fruits.clear()
    print(f"#2 Clear fruits successfully!")

print("\n\n")
#3
current_users = usernames
new_users = ['benidict', 'naruto', 'nina', 'hinata', 'sakura', 'nino', 'NARUTO']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"username {new_user} is already used, please enter new username!")
    else: 
        print(f"{new_user}, is available!")

print("\n\n")
#4
numbers = [1,2,3,4,5,6,7,8,9]
identifier = []
for number in numbers:
    if number == 1:
        identifier = "st"
    elif number == 2:
        identifier = "nd"
    elif number == 3:
        identifier = "rd"
    else:
        identifier = "th"

    print(f"{number}{identifier}")
