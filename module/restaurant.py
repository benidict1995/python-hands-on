class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, cuisine_description):
        """Initialized restaurant class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.cuisine_description = cuisine_description

    def display_restaurant_name(self):
        """Display restaurant name"""
        print(f"Welcome to {self.restaurant_name}")

    def display_cuisine(self):
        """Display cuisine"""
        print(f"\n{self.cuisine_type.title()}")
        print(f"Common Dishes:\n{self.cuisine_description.title()}")