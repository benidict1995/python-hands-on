
class Employee:
    """Employee Information"""
    
    def __init__(self, first_name = 'Benidict', last_name = 'Dulce', annual_salary = '12000000', salary_raise = '5000'):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.salary_raise = salary_raise

    def give_raise(self, salary_raise = '5000'):
        """Give employee raise"""
        new_salary = int(salary_raise) + int(self.annual_salary)
        return new_salary


# employee = Employee()
# new_salary_raise = employee.give_raise('10000')
# print(f"Hi {employee.first_name} {employee.last_name} you have raise {new_salary_raise}")
