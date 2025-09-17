numbers = [1, 8, 27, 64, 125, 216, 343, 512, 729]
print(f"The first three items in the list are:{numbers[:3]}")
print(f"Three items from the middle of the list are:{numbers[3:6]}")
print(f"The last three items in the list are:{numbers[6:9]}\n")

flavore = ['pepperoni',
'hawaiian',
'four cheese',
'bbq chicken',
'veggie',
'margherita',
'meat lovers']

my_pizza = flavore
friend_pizza = flavore[:3]
my_pizza.append("my pizza flavore")
friend_pizza.append("friend pizza flavore")
print(f"my pizza:{my_pizza}\n")
print(f"friend pizza:{friend_pizza}")

print("\n\nMy pizza flavore:")
for pizza in my_pizza:
    print(f"- {pizza}")

print("\nMy friend pizza flavore:")
for pizza in friend_pizza:
    print(f"-{pizza}")
