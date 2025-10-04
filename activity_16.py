#1
people_0 = {'fname': 'benidict', 'lname': 'dulce'}
people_1 = {'fname': 'nina', 'lname': 'adlawan'}
people_2 = {'fname': 'nino', 'lname': 'aso'}
peoples = [ people_0, people_1, people_2]
for people in peoples:
    print(f"fullname: {people['fname'].title()} {people['lname'].title()}")

print("\n")
#2
pet_0 = {'owner': 'benidict', 'pet':  {  'name': 'conan', 'kind': 'dog',  'breed': 'american bully'}}
pet_1 = {'owner': 'nina', 'pet':  {  'name': 'nino', 'kind': 'dog',  'breed': 'shi tzu'}}
pet_2 = {'owner': 'singgangger', 'pet':  {  'name': 'albino', 'kind': 'bird',  'breed': 'green bird'}}
pets = [
    pet_0,
    pet_1,
    pet_2
]
for info in pets:
    print(f"Owner: {info['owner'].title()}")
    for label, pet in info['pet'].items():
        print(f"\t{label}: {pet.title()}")
    print("\n")

print("\n")
#3
favorite_places = {
    'benidict': ['america', 'philippines', 'japan'],
    'nina': ['korea', 'canada', 'philippines'],
    'nino': ['philippines', 'china', 'singapore'],
}

for name, places in favorite_places.items():
    count = 0
    print(f"Hi {name.title()}, Your favorite places are: ")
    for place in places:
        count += 1
        print(f"\t{count}.{place.title()}.")
    print("\n")

print("\n")
#4
favorite_numbers = {
    'benidict': [47, 2, 100],
    'nina': [20, 7, 12],
    'nino': [3, 1, 2],
}

for name, numbers in favorite_numbers.items():
    print(f"Hi {name.title()}, Your favorite numbers are: ")
    for number in sorted(numbers):
        print(f"\t{number}")
    print("\n")

print("\n")
#4
cities = {
    "tokyo": {
        "country": "japan",
        "population": "37 million",
        "fact": "Tokyo is the largest metropolitan area in the world."
    },
    "paris": {
        "country": "france",
        "population": "11 million",
        "fact": "Paris is known as the City of Light and home to the Eiffel Tower."
    },
    "cairo": {
        "country": "egypt",
        "population": "20 million",
        "fact": "Cairo is located on the Nile River and is near the Great Pyramids of Giza."
    }
}
for city, info in cities.items():
    print(f"{city.title()}")
    print(f"{info['fact']}, It is from {info['country']} with total population of {info['population']}.\n")

print("\n")
#5

for city, info in cities.items():
    if city == "tokyo":
        cities[city]["founded_year"] = 1603
        cities[city]["language"] = "Japanese"
    elif city == "paris":
        cities[city]["founded_year"] = -52
        cities[city]["language"] = "French"
    elif city == "cairo":
        cities[city]["founded_year"] = 969
        cities[city]["language"] = "Arabic"

if "new york" not in cities:
    cities["new york"] = {
        "country": "USA",
        "population": "19 million",
        "fact": "New York City is home to the Statue of Liberty.",
        "founded_year": 1624,
        "language": "English",
    }

for city, info in cities.items():
      print(f"{city.title()}")
      print(f"{info['fact']}, It is from {info['country']} with total population of {info['population']}, {city.title()} founded in {info['founded_year']} and their mother language is {info['language']}.\n")

