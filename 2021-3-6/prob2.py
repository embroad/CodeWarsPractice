# CodeWars 2021 Problem 2 | 3-6-21
# Emily Broad and Sierra Janson
# V = π * z * z * h (π = 3.1415926536)

import sys
import math

file = open("CodeWars\prob2.txt",'r')
dimensions = []
for line in file:
    dimensions = line.split()
# print dimensions

h = dimensions[0]
z = dimensions[1]
# print(h,z)
pi = float(3.1415926536)

V = pi * float(z) * float(z) * float(h)
print(f"{V:.2f} cubic inches")
