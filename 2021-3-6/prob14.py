# CodeWars 2021 Problem 14 | 3-6-21
# Emily Broad and Sierra Janson

# You will receive on a line 3 integers (or fractions) separated by spaces. The first number will be the number of
# sticks of dynamite. The second will be the size of the stick (1/4, 1/3, 1/2, 1, 2 or 3). The third number will be the
# tensile limit (in Megajoules (MJ)) the Mask can tolerate at that moment

from fractions import Fraction

my_File = open("CodeWars\prob14.txt",'r')
data = []
for line in my_File:
    data = line.split()
# print(data)

num_Sticks = data[0]
stick_Size = data[1]
tensile_Limit = data[2]

num_Sticks = float(sum(Fraction(s) for s in num_Sticks.split()))
stick_Size = float(sum(Fraction(s) for s in stick_Size.split()))
tensile_Limit = float(sum(Fraction(s) for s in tensile_Limit.split()))

# 7.5MJ of explosive force are released when 1kg of dynamite explodes.

total_Sticks = float(num_Sticks) * float(stick_Size)
# print(total_Sticks)

explosive_Mass = total_Sticks * 0.45
explosive_Force = explosive_Mass * 7.5
# print(explosive_Force)

if explosive_Force <= float(tensile_Limit):
    print(f"{explosive_Force:.2f} the Mask can eat it!")
else:
    print(f"{explosive_Force:.2f} the Mask should not eat it!")
