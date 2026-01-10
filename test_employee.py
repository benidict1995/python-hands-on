import pytest
from employee import Employee

@pytest.fixture
def employee_instance():
    """Employee object"""
    employee_info = Employee()
    return employee_info


def test_employee_raise_10000(employee_instance):
    """Employee raise to 10,000"""
    new_raise = employee_instance.give_raise('10000')
    assert 12010000 == new_raise