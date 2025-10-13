#1
def make_sandwich(*args):
    """Print a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in args:
        print(f"- {item}")


make_sandwich('ham', 'cheese', 'lettuce')
make_sandwich('tuna', 'mayo')
make_sandwich('egg', 'bacon', 'tomato', 'avocado')

#2
print("\n")
def build_profile(fname, lname, **profile):
    profile['first_name'] = fname
    profile['last_name'] = lname
    """Create profile"""
    print(profile)

build_profile("benidict", "dulce", age = "30", height = "5'5", width = "73kg")

#3
print("\n")
cars = []
def make_car(car_manufacturer, car_model, **car_info):
     """Build a dictionary containing everything we know about a car."""
     car_info['manufacturer'] = car_manufacturer
     car_info['model'] = car_model
     return car_info

car1 = make_car("toyota", "vios", color = "black", size = "sedan") 
car2 = make_car("honda", "civic", color = "white", size = "sedan") 
car3 = make_car("ford", "ranger", color = "gray", size = "4x4") 
cars.append(car1)
cars.append(car2)
cars.append(car3)

print(cars)
