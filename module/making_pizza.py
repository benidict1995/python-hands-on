# import pizza as p (import pizza file with function inside and add alias as P)
# import pizza (import all function and use it as pizza.make_pizza)
# from pizza import make_pizza (import specific function)
# from pizza import * (import all the functions)
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')