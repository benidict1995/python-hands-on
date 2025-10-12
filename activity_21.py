#1
def make_shirt(shirt_message, shirt_size = 'large'):
    print(f"{shirt_message} {shirt_size.title()}")

make_shirt("The size of the shirt is", "medium")
make_shirt("My size of the shirt is")

#2
print("\n")
def describe_city(city_name, country = 'philippines'):
    print(f"{city_name.title()} is in {country.title()}")

describe_city("cavite")
describe_city("tokyo", "japan")
describe_city("paris", "france")
describe_city("toronto", "canada")