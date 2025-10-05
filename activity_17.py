#1
car = input("Do we know what kind of car do you want to rent? ")
print(f"Let me see if I can find you a {car}.")

print("\n")
#2
customer = input("How many are you in the group? ")
if int(customer) > 8:
    print("You have to wait for a table.")
else:
    print("The table is ready.")

print("\n")
#3
number = input("Enter number that are multiple by 10: ")
if int(number) % 10:
    print(f"The number {number} is not multiple of 10.") 
else :
    print(f"The number {number} is a multiple of 10.") 
