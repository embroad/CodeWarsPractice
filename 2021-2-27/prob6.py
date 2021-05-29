# CodeWars 2021 Problem 6 | 2-27-21
# Emily Broad and Sierra Janson

# P^2 == R^3
# R == P^(2/3)
# R == semi-orbital radius
# P == orbital period

# pull in data, get rid of zero
# R == P^(2/3)
# round to .0001 
# shove in list
# print it
import sys
import math

file = open("2-27-2021\prob6.txt", "r")
input_data = []
for line in file:
    input_data.append(line.strip())
input_data.pop()


output_data = []
for i in input_data:
    i = float(i)
    output_data.append(i ** (2/3))

for i in output_data:
    print(round(i,4))
