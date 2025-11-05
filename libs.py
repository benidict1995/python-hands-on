from random import randint
from random import choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']

num = randint(1, 6)
first_up = choice(players)

print(f"{num}")
print(f"{first_up}")