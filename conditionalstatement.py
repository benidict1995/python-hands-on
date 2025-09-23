age = 19
if age > 18:
    print("You are now a voter!")
else:
    print("You are not a voter!")

print("\n\n")

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

print("\n\n")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Mushrooms is already added.")
if 'pepperoni' != requested_toppings:
    print("Adding pepperoni to the list.")

print("\n\n")

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"We don't have {requested_topping}")

print("\nFinish making your pizza!")