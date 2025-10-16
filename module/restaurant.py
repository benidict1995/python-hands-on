class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, cuisine_description, number_serve = 0):
        """Initialized restaurant class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.cuisine_description = cuisine_description
        self.number_serve = number_serve

    def display_restaurant_name(self):
        """Display restaurant name"""
        print(f"Welcome to {self.restaurant_name}")

    def display_cuisine(self):
        """Display cuisine"""
        print(f"\n{self.cuisine_type.title()}")
        print(f"Common Dishes:\n{self.cuisine_description.title()}")

    def display_number_serve(self):
        """Serve's Monitor"""
        print(f"Serving {self.number_serve}")

    def set_number_served(self, number):
        """Set number to be served"""
        self.number_serve = number

    def increment_number_served(self, number):
        """Increment number to be served"""
        self.number_serve += number
    

    