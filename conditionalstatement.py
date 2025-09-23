age = 19
if age > 18:
    print("You are now a voter!")
else:
    print("You are not a voter!")

ride_age = 5
if ride_age < 4:
    print("Your admission cost is $0.")
elif ride_age < 18:
    print("Your admission cost is $25.")
else: 
    print("Your admission cost is $40.")

price = 0
age_price = 19
if age_price < 4:
    price = 0
elif age_price < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost base on the age is ${price}.")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Mushrooms is already added.")
if 'pepperoni' is not requested_toppings:
    print("Adding pepperoni to the list.")