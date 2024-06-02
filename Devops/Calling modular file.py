# Import the File module my_module.py
# Selective import 

from my_module import sum,mul
from my_module import *
import my_module as m

print(m.cube(5))

print(m.sum(5, 6))

print(m.mul(5, 6))


