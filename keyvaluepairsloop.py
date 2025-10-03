#1
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for k, v in user_0.items():
    print(f"key:{k}, value:{v}")


#2
print("\n")
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#3
print("\n")
for name in favorite_languages.keys():
    print(f"{name}")
print("\n")
for value in favorite_languages.values():
    print(f"{value}")
print("\n")
persons = ['phil', 'sarah']
for name in favorite_languages.keys():
    if name in persons:
        language = favorite_languages[name].title()
        print(f"I see you {name.title()}, your favorite language is {language}")
print("\n")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, Thank you for your hardwork!")