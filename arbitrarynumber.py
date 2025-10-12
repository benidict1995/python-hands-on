def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping} {size}'")

make_pizza(16, 'pepperoni')
make_pizza(14, 'mushrooms', 'green peppers', 'extra cheese')