#1
person = {'first_name': 'benidict', 'last_name': 'dulce', 'age': 1, 'city': 'Mundo City'}
print(f"First name:{person['first_name'].title()}")
print(f"Last name:{person['last_name'].title()}")
print(f"Age:{person['age']}")
print(f"City:{person['city']}")

print("\n")
#2
favorite_number = {'benidict': 2, 'nina': 100, 'rd': 50, 'leo': 10, 'reyland': 5}
print(f"Hi Benidict, your favorite number is {favorite_number['benidict']}")
print(f"Hi Nina, your favorite number is {favorite_number['nina']}")
print(f"Hi RD, your favorite number is {favorite_number['rd']}")
print(f"Hi Leo, your favorite number is {favorite_number['leo']}")
print(f"Hi Reyland, your favorite number is {favorite_number['reyland']}")

print("\n")
#3
glossary = {'kotlin': 'programming language for Android development', 'xcode': 'programming language for iOS development',
            'php': 'programming language for Web development', 'c#': 'programming language for Web development', 'python': 'programming for Web development.'}
for gloss in glossary:
    print(f"{gloss}: ${glossary[gloss]}\n")
