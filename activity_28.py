from module.restaurant import Restaurant
from module.user import User
from privileges import Privileges
from electric_car import Battery

#1
class IceCreamStand(Restaurant):
    """Ice Cream Stand"""
    def __init__(self, restaurant_name = "Ice Cream Stand", cuisine_type = "ice cream", cuisine_description = ""):
        super().__init__(restaurant_name= restaurant_name, cuisine_type=cuisine_type, cuisine_description=cuisine_description)
        self.flavours = ["Vanilla", "Chocolate", "Strawberry"]
        
    def display_flavors(self):
        """Ice Cream Flavours"""
        for flavour in self.flavours:
            print(f"- {flavour}")

menu  = IceCreamStand()
menu.display_restaurant_name()
menu.display_flavors()
print("\n")
#2
class Admin(User):
    """Administration"""
    def __init__(self, first_name = "Benidict", last_name = "Dulce", attemp=0):
        super().__init__(first_name, last_name, attemp)
        #3
        self.perks = Privileges(privileges = ["can add post", "can add post", "can ban user"])
        #4
        self.battery = Battery()


admin = Admin()
print(f"Hi Admin {admin.display_first_name()} {admin.display_last_name()},\nPlease check your privileges below:")

#3
admin.perks.show_privileges()

#4
print("\n")
admin.battery.battery_size = 40
print(f"Hi Admin, your Electric Car battery is {admin.battery.battery_size}")
admin.battery.get_range()
print(f"\nUpgrading your battery to 65")
admin.battery.upgrade_battery(size = 65)
admin.battery.get_range()