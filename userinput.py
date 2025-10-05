#name = input("Please enter your name: ")
# print(f"Hello, {name}\n\n")

#prompt = "If you share your name, we can personalize the messages you see."
#prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")


# print("\n")
# age = input("How old are you? ")
# if int(age) >= 18:
#     print("You are old")
# else:
#     print("You are child")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")