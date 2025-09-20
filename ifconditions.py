cars = ['toyota', 'bmw', 'honda']
for car in cars: 
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title()) 



requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")


toppings = ['mushrooms', 'onions', 'pineapple']
isExists = 'mushrooms' in toppings
print(f"isExists:{isExists}")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, is not banned!")
else :
    print("The user is Banned!")