#1, 2
from module.restaurant import Restaurant
from module.user import User

resto = Restaurant(restaurant_name="Dulce de Cafe", cuisine_type="Filipino Cuisine", cuisine_description="Adobo, Sinigang, Kare-kare, Lumpia")

resto.display_restaurant_name()
resto.display_cuisine()

print("\n")
resto.restaurant_name = "Dolche de Cafe"
resto.cuisine_type = "Italian Cuisine"
resto.cuisine_description = "Pasta, Pizza, Lasagna, Risotto"
resto.display_restaurant_name()
resto.display_cuisine()

print("\n")
resto.restaurant_name = "Tande bayo"
resto.cuisine_type = "Japanese Cuisine"
resto.cuisine_description = "Sushi, Ramen, Tempura, Teriyaki"
resto.display_restaurant_name()
resto.display_cuisine()

print("\n")
user = User(first_name="benidict", last_name="dulce")
print(f"{user.display_first_name()} {user.display_last_name()}")

print("\n")
user.first_name = "nina"
user.last_name = "adlawan"
print(f"{user.display_first_name()} {user.display_last_name()}")

