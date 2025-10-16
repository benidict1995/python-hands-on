class Car:

    def __init__(self, make, model, year):
        """Initialized car class"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, odo):
            """Update the car's mileage."""
            if odo >= self.odometer_reading:
                self.odometer_reading += odo
            else:
                print("You can't roll back an odometer!")