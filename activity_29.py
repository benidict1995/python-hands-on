from module.restaurant import Restaurant
from module.user import User, Privileges, Admin

resto = Restaurant(restaurant_name="Dulce de Cafe", cuisine_type="Filipino Cuisine", cuisine_description="Adobo, Sinigang, Kare-kare, Lumpia", number_serve=46)
resto.display_restaurant_name()


privilege = Privileges("Block User")
admin = Admin("Benidict")

admin.show_admin_name()
privilege.show_privilege()