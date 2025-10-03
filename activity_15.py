#1
favorite_language = {
    'ph': 'this is philippines',
    'au': 'this is Australia',
    'us': 'this is US',
    'nz': 'this is New Zealand'
}

for k, v in favorite_language.items():
    print(f"{k}, {v}")

#2
countries = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
    "mississippi": "united states",
    "ganges": "india",
    "danube": "germany",
    "mekong": "vietnam",
    "volga": "russia",
    "thames": "united kingdom",
    "seine": "france"
}
print("\n")
for k, v in countries.items():
    print(f"{k.title()} is {v.title()}")

print("\n")
#3
# people who should take the poll (mix of taken + not taken)
people_to_poll = ['jen', 'edward', 'anna', 'mark', 'tom']
persons = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for k, v in persons.items():
    if k in people_to_poll:
        print(f"Hi {k.title()}, you are already invited in {v.title()} talk!")
    else:
        print(f"Hi {k.title()}, please check your email and accept the invitation!")
