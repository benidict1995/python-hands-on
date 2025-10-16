#1
from module.restaurant import Restaurant
from module.user import User

resto = Restaurant(restaurant_name="Dulce de Cafe", cuisine_type="Filipino Cuisine", cuisine_description="Adobo, Sinigang, Kare-kare, Lumpia", number_serve=46)

resto.display_restaurant_name()
resto.display_number_serve()
resto.set_number_served(50)
resto.display_number_serve()
resto.increment_number_served(2)
resto.display_number_serve()

#2
print("\n")
user = User("benidict", "dulce")
print(f"Hello, {user.display_first_name()} {user.display_last_name()}")
print(f"Login attemp is {user.display_login_attemp()}")
print(f"Attempting login... {user.increment_login_attemp(1)}")
print(f"Login attemp is {user.display_login_attemp()}")
print(f"Attempting login... {user.increment_login_attemp(1)}")
print(f"Login attemp is {user.display_login_attemp()}")
print(f"Login successful, now resetting login attemp... ")
user.reset_login_attemp()
print(f"Login attemp... {user.display_login_attemp()}")
