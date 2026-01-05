from city_country import formatted_address

def test_city_country_address():
    formatted = formatted_address("cavite", "philippines")
    assert formatted == 'Cavite, Philippines'