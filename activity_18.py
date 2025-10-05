#1
# message = ""
# pizza = []
# pizza_toppings = ["pepperoni", "mushrooms", "onions", "sausage", "bacon", "extra cheese", "black olives", "green peppers", "pineapple", "spinach"]
# print("Toppings Menu:")
# for p in pizza_toppings:
#     print(f"* {p.title()}")

# print("\n")
# question = "Choose toppings: "
# toppings = input(question)
# while True:
#     message = toppings
#     if message == 'quit':
#         break
#     else :
#         if toppings.lower() in pizza_toppings:
#             if (toppings.lower() in pizza):
#                 print(f"{toppings.title()} is already added!")
#             else :
#                 pizza.append(toppings)
#                 print(f"{toppings.title()} added!")
#         else:
#             print(f"{toppings.title()} not available!")
#         toppings = input(question)

# print(f"Your pizza toppings {pizza}")


#2
print("Ticket Price:")
menu = {'kids': 'free', 'teen': '$10', 'adult': '$15'}
for k, v in menu.items():
    print(f"{k.title()} - {v}")
print("\nEnter 'quit' to exit\n")
question = "Enter your age: "
age = input(question)
while True:
    message = age
    if message == 'quit':
        break
    else:
        if int(age) < 3:
            print("Hey kids, You are free!")
        elif int(age) >= 3 and int(age) <= 12:
            print("Hey teen, your ticket is $10.")
        else :
            print("Hey adult, your ticket is $15.")
    age = input(question)