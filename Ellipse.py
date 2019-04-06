# import matplotlib.pyplot as plt
import numpy as np
import sympy
from sympy import *
# from matplotlib.patches import Ellipse


h = float(input("What is the h value?: "))
underX = float(input("What is the value under x?: "))

k = float(input("What is the k value?: "))
underY = float(input("What is the value under y?: "))


if underX > underY:
    a2 = underX
    b2 = underY
    a = sympy.sqrt(a2)
    b = sympy.sqrt(b2)
else:
    a2 = underY
    b2 = underX
    a = sympy.sqrt(a2)
    b = sympy.sqrt(b2)

c2 = a2 - b2
c = sympy.sqrt(c2)
foci = "The foci are at: ({}, {} + {}) and ({}, {} + {})".format(h, k, c, h, k, c)
print(foci)
