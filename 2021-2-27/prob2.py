# CodeWars 2021 Problem 2 | 2-27-21
# Emily Broad and Sierra Janson

# Pe = C * P

file = open("2-27-2021\prob2.txt", "r")
input_data = []
for line in file:
    input_data.append(line)
C = input_data[0]
P = input_data[1]
Pe = int(C) * int(P)
print(Pe)

# for line in file:
#     for i in range(0,1):
#         global C
#         C = int(line)

# for line in file:
#     for i in range(2):
#         global P
#         P = int(line)

# print(C * P)
