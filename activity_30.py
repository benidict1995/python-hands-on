import random
import string
from random import choice

#1
# class Die:
#     """A simple die class."""

#     def __init__(self, sides=6):
#         self.sides = sides

#     def roll_die(self):
#         """Print a random number between 1 and the number of sides."""
#         print(random.randint(1, self.sides))


# # 6-sided die
# print("Rolling a 6-sided die:")
# six_sided = Die()
# for _ in range(10):
#     six_sided.roll_die()

# print("\nRolling a 10-sided die:")
# ten_sided = Die(10)
# for _ in range(10):
#     ten_sided.roll_die()

# print("\nRolling a 20-sided die:")
# twenty_sided = Die(20)
# for _ in range(10):
#     twenty_sided.roll_die()

#2


combination = [str(i) for i in range(10)] + list(string.ascii_lowercase)
class Lottery:
    """Init Lottery Class"""
    def __init__(self, data = []):
        self.data = data
    

    def draw(self):
        """Draw lottery"""
        
        result = ""
        x = 1
        while x < 5:
            result += choice(combination).capitalize()
            x += 1

        print(f"Final draw: {result}")


lottery = Lottery()
lottery.draw()

