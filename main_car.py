import car

car_clazz = car.Car(make = "toyota", model = "vios", year = "2020")
car_clazz.odometer_reading = 20000
print(f"{car_clazz.get_descriptive_name()}")
car_clazz.read_odometer()

print("\n")
car_clazz.make = "honda"
car_clazz.model = "civic"
car_clazz.year = "2017"
car_clazz.odometer_reading = 100
print(f"{car_clazz.get_descriptive_name()}")
car_clazz.read_odometer()

car_clazz.update_odometer(300)
car_clazz.read_odometer()

