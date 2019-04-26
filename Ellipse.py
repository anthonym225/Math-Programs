# import matplotlib.pyplot as plt
import numpy as np
import sympy
from sympy import *
# from matplotlib.patches import Ellipse


h = float(input("What is the h value?: "))
underX = float(input("What is the value under x?: "))

k = float(input("What is the k value?: "))
underY = float(input("What is the value under y?: "))

# Horizontal or Vertical Major Axis
if underX > underY:
    majorAxis = "The Major Axis follows the X axis"
    a2 = underX
    b2 = underY
    a = sympy.sqrt(a2)
    b = sympy.sqrt(b2)
    c2 = a2 - b2
    c = sympy.sqrt(c2)
    foci = "The foci are at: ({}, {} + {}) and ({}, {} - {})".format(h, k, c, h, k, c)
    vertices = "The vertices are at: ({}, {}) and ({}, {})".format(h + a, k, h - a, k)
    print(majorAxis)
    print(foci)
    print(vertices)
else:
    majorAxis = "The Major Axis follows the Y axis"
    a2 = underY
    b2 = underX
    a = sympy.sqrt(a2)
    b = sympy.sqrt(b2)
    c2 = a2 - b2
    c = sympy.sqrt(c2)
    foci = "The foci are at: ({} + {}, {}) and ({} - {}, {})".format(h, c, k, h, c, k)
    vertices = "The vertices are at: ({}, {}) and ({}, {})".format(h + a, k, h - a, k)
    print(majorAxis)
    print(foci)
    print(vertices)
