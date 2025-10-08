#1
sandwiches = ['cheese sandwich', 'pastrami','peanut sandwich', 'pastrami','korean sandwich', 'tuna sandwich', 'pastrami']
finished_sandwiches = []

for sandwich in sandwiches:
    print(f"We currently made your {sandwich.title()}")
    finished_sandwiches.append(sandwich)

print("\nDone Order:")
while finished_sandwiches:
    print(finished_sandwiches.pop().title())

#2
print("\nWe run out of stock for 'Pastrami': ")
while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')
    print(f"Removing pastrami from your order...")

print("\nUpdating your order: ")
while sandwiches:
    print(sandwiches.pop().title()) 

#3
print("\nPoll for your dream destination")
responses = []
poll_active = True
while poll_active:
    destination = input("Enter your dream destination: ")
    response = [destination]
    responses.append(destination)
    repeat = input("Would you like to add more? (yes/ no) ")
    if repeat == 'no':
        break


print("\nPoll result:")
for dream in responses:
    print(f"{dream.title()}")