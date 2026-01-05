
def formatted_address(city, country, population = ''):
    if population:
        user_address = f"{city}, {country}".title()
        address = f"{user_address} with {population} people."
    else:
        address = f"{city}, {country}".title()
    return address
