from name_function import get_formatted_name

def test_first_last_middle_name():
    formatted_name = get_formatted_name('ben', 'dul', 'vel')
    assert formatted_name == 'Ben Vel Dul'