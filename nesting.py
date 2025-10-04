#1
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print(f"Total number of aliens:{len(aliens)}")

print("\n")
#2
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# Summarize the order.
count = 0
print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings:")
for topping in pizza['toppings']:
    count +=1
    print(f"\t{count}.{topping}")

print("\n")
#3
favorite_languages = {
    'ben': ['kotlin', 'c++', 'python', 'java', 'javascript'],
    'leo': ['c#', 'javascript', 'php'],
    'nina': ['php', 'java']
}

for name, languages in favorite_languages.items():
    count = 0
    print(f"{name.title()} favorite languages:")
    for language in languages:
        count += 1
        print(f"{count}. {language.title()}")

print("\n")
#4
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, userInfo in users.items():
    print(f"{username.title()},")
    for title, info in userInfo.items():
        print(f"\t{title}: {info.title()}")