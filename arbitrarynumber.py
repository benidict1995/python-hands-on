#1
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping} {size}'")

make_pizza(16, 'pepperoni')
make_pizza(14, 'mushrooms', 'green peppers', 'extra cheese')

#2
print("\n")
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)