from city_country import formatted_address

def test_city_country_population():
    address = formatted_address("cavite", "philippines", "3,000,000")
    assert address == 'Cavite, Philippines with 3,000,000 people.'