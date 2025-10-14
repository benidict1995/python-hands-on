import animal 


dog = animal.Dog(name = "nino", age = "1")
print(f"My dog's name is {dog.name.title()}.")
print(f"My dog is {dog.age} years old.")


print("\n")
dog.sit()
dog.roll_over()

your_dog = animal.Dog('lucy', 3)
print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")


print("\n")
your_dog.sit()
your_dog.roll_over()