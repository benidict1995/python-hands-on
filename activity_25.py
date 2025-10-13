#1, 2
import module.printing_functions as pf
from module.printing_functions import full_name
from module.printing_functions import full_name as fn
#from printing_functions import *

name = pf.full_name("benidict", "dulce")
print(f"Your name is {name}")

name0 = fn("nina", "dulce")
print(f"Your name is {name0}")

name1 = full_name("nino", "dulce")
print(f"Your name is {name1}")