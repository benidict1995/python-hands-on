class User:

    def __init__(self, first_name, last_name, attemp = 0):
        """Initialized user class"""
        self.first_name = first_name
        self.last_name = last_name
        self.attemp = attemp

    def display_first_name(self):
        return self.first_name.title()

    def display_last_name(self):
        return self.last_name.title()
    
    def increment_login_attemp(self, attemp):
        """Incrementing login attemp..."""
        self.attemp += attemp
        return self.attemp

    def reset_login_attemp(self): 
        """Resetting login attemp..."""
        self.attemp = 0
    
    def display_login_attemp(self):
        """Displaying login attemp..."""
        return self.attemp