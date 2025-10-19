class Privileges():
    """Show list of privileges"""
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """Show list of privileges"""
        for privil in self.privileges:
            print(f"- {privil}")